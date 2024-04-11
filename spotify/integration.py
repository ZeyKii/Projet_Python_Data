import json
import timeit
import pathlib
import duckdb

from rich.pretty import pprint


def create_db_connection():
    try:
        conn = duckdb.connect('D:\Repo\Projet_Python_Data\playlists.db')
        return conn
    except Exception as e:
        print("Une erreur est survenue lors de la connexion à la base de données :", e)


def show_tables(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
            tables = cursor.execute("SHOW TABLES;").fetchall()
            print("Liste des tables dans la base de données :")
            for table_name in tables:
                print(table_name[0])
            cursor.close()
        except Exception as e:
            print("Une erreur est survenue: {}".format(e))
    else:
        print("Impossible de se connecter à la base de données.")



def create_or_refresh_db(conn):
    if conn is not None:
        try:

            cursor = conn.cursor()

            drop_table_queries = [
                "DROP TABLE IF EXISTS Tracks;",
                "DROP TABLE IF EXISTS Albums;",
                "DROP TABLE IF EXISTS Artists;",
                "DROP TABLE IF EXISTS Playlists;",
            ]

            for query in drop_table_queries:
                cursor.execute(query)

            create_table_queries = [
                """
                CREATE TABLE Playlists (
                    pid INT PRIMARY KEY,
                    name VARCHAR(255),
                    collaborative BOOLEAN,
                    modified_at TIMESTAMP,
                    num_tracks INT,
                    num_albums INT,
                    num_followers INT,
                    num_edits INT,
                    duration_ms BIGINT,
                    num_artists INT
                );
                """,
                """
                CREATE TABLE Artists (
                    artist_uri VARCHAR(255) PRIMARY KEY,
                    artist_name VARCHAR(255)
                );
                """,
                """
                CREATE TABLE Albums (
                    album_uri VARCHAR(255) PRIMARY KEY,
                    album_name VARCHAR(255),
                    artist_uri VARCHAR(255),
                    FOREIGN KEY (artist_uri) REFERENCES Artists(artist_uri)
                );
                """,
                """
                CREATE TABLE Tracks (
                    track_uri VARCHAR(255) PRIMARY KEY,
                    track_name VARCHAR(255),
                    duration_ms BIGINT,
                    pos INT,
                    pid INT,
                    album_uri VARCHAR(255),
                    FOREIGN KEY (pid) REFERENCES Playlists(pid),
                    FOREIGN KEY (album_uri) REFERENCES Albums(album_uri)
                );
                """,
            ]

            for query in create_table_queries:
                cursor.execute(query)

            cursor.close()

            print("Les tables ont été correctement supprimées et recréées.")

        except Exception as e:
            if e.errno == e.ER_ACCESS_DENIED_ERROR:
                print(
                    "Quelque chose ne va pas avec votre nom d'utilisateur ou mot de passe"
                )
            elif e.errno == e.ER_BAD_DB_ERROR:
                print("La base de données n'existe pas")
            else:
                print(e)


def bulk_insert_playlists(conn, playlists):
    cursor = conn.cursor()
    insert_query = """
    INSERT OR IGNORE INTO Playlists (pid, name, collaborative, modified_at, num_tracks, num_albums, num_followers, num_edits, duration_ms, num_artists)
    VALUES (?, ?, ?, to_timestamp(?), ?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(insert_query, playlists)
    conn.commit()
    cursor.close()


def bulk_insert_albums(conn, albums):
    cursor = conn.cursor()
    insert_query = """
    INSERT IGNORE INTO Albums (album_uri, album_name, artist_uri)
    VALUES (?, ?, ?)
    """
    cursor.executemany(insert_query, albums)
    conn.commit()
    cursor.close()


def bulk_insert_artists(conn, artists):
    cursor = conn.cursor()
    insert_query = """
    INSERT IGNORE INTO Artists (artist_uri, artist_name)
    VALUES (?, ?)
    """
    cursor.executemany(insert_query, artists)
    conn.commit()
    cursor.close()


def bulk_insert_tracks(conn, tracks):
    cursor = conn.cursor()
    insert_query = """
    INSERT IGNORE INTO Tracks (track_uri, album_uri, track_name, duration_ms, pos, pid)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    cursor.executemany(insert_query, tracks)
    conn.commit()
    cursor.close()


    # Bulk insert dans la table d'associations PlaylistTrack


def extract_json(filepath, conn):
    with open(filepath, "r") as f:
        data = json.load(f)
        artists = set()
        tracks = set()
        albums = set()
        playlists = set()
        # nouveau set de la table d'association
            # clef étrangère "pid" de la playlist
            # clef étrangère "track_uri" de la track
        for i, playlist in enumerate(data["playlists"], start=1):
            # print(f"Playlist n°{i}/{len(data["playlists"])}: {playlist["name"]}")
            playlists.add(
                (
                    playlist["pid"],
                    playlist["name"],
                    playlist["collaborative"],
                    playlist["modified_at"],
                    playlist["num_tracks"],
                    playlist["num_albums"],
                    playlist["num_followers"],
                    playlist["num_edits"],
                    playlist["duration_ms"],
                    playlist["num_artists"],
                )
            )
            for track in playlist["tracks"]:
                artists.add((track["artist_uri"], track["artist_name"]))
                tracks.add(
                    (
                        track["track_uri"],
                        track["album_uri"],
                        track["track_name"],
                        track["duration_ms"],
                        track["pos"],
                        playlist["pid"],
                    )
                )
                albums.add(
                    (track["album_uri"], track["album_name"], track["artist_uri"])
                )

                # pprint(playlists)
                # pprint(tracks)
                # pprint(albums)
                # pprint(artists)
                # break
            # break

        print("Insertion des playlists...")
        bulk_insert_playlists(conn, list(playlists))
        # print("Insertion des artistes...")
        # bulk_insert_artists(conn, list(artists))
        # print("Insertion des albums...")
        # bulk_insert_albums(conn, list(albums))
        # print("Insertion des tracks...")
        # bulk_insert_tracks(conn, list(tracks))

        # Appel au bulk insert de PlaylistTrack


def process_json_files(conn):
    source_dir = pathlib.Path(__file__).resolve().parent / "sources"
    for i, element in enumerate(source_dir.iterdir(), start=1):
        if element.is_file():
            print(f"Fichier: {element}")
            extract_json(element, conn)
        if i == 10:
            break


def main():
    conn = create_db_connection()

    time = timeit.timeit(lambda: create_or_refresh_db(conn), number=1)
    print(f"Création/refresh : {time:.3f} secondes")

    time = timeit.timeit(lambda: show_tables(conn), number=1)
    print(f"Vérification des tables : {time:.3f} secondes")

    time = timeit.timeit(lambda: process_json_files(conn), number=1)
    print(f"Intégration des données : {time:.2f} secondes")

    conn.close()

if __name__ == "__main__":
    main()