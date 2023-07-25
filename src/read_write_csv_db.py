import pandas as pd


def write_to_file():
    raw_data = {
        "name": ['Oveys', 'Ala', 'Mohammad'],
        "height": [1.74, 1.64, 1.67],
        "weight": [73, 54, 48]
    }
    frame = pd.DataFrame(raw_data)
    # print(frame.iloc[0])
    # print(frame["name"])

    bmi = [
        frame["weight"][i] / (frame["height"][i] ** 2)
        for i in range(len(frame))
    ]

    frame["bmi"] = bmi
    # frame.to_csv('bmi.csv', index=False, sep="\t")
    frame.to_csv('bmi.csv', sep="\t")
    print(frame)


def read_from_file():
    frame = pd.read_csv('bmi.csv', sep="\t", usecols=[1, 2, 3])
    print(frame)


def read_from_db():
    import sqlite3

    # conn = sqlite3.connect('gta.db')
    # c = conn.cursor()
    #
    # c.execute(
    #     '''
    #       CREATE TABLE IF NOT EXISTS persons
    #       (
    #            [person_id] INTEGER PRIMARY KEY,
    #            [person_name] TEXT,
    #            [person_city] TEXT,
    #            [person_age] INTEGER
    #        )
    #     '''
    # )
    #
    # c.execute(
    #     '''
    #       INSERT INTO persons (person_id, person_name, person_city, person_age)
    #
    #             VALUES
    #             (1,'OVEYS', 'RASHT', 29),
    #             (2,'Mohammad', 'TEH', 30),
    #             (3,'Ala', 'RASHT', 30),
    #             (4,'Javid', 'TEH', 30),
    #             (5,'Mobin', 'RASHT', 18)
    #       '''
    # )
    # conn.commit()

    connection = sqlite3.connect('gta.db')
    frame = pd.read_sql("SELECT * FROM persons", connection)
    # print(frame.head()) # first 5 rows
    # print(frame.tail(2)) # last 2 rows

    # print(frame[frame["person_city"] == "TEH"])

    # replaced_frame = frame.replace("RASHT", "R")
    # replaced_frame = replaced_frame.replace("TEH", "T")
    # print(replaced_frame)

    ''' Axis 1 is for columns and axis 0 is for rows '''
    # cleaned_frame = frame.drop('person_city', axis=1)
    # cleaned_frame = frame.drop(['person_city', 'person_age'], axis=1)
    # print(cleaned_frame)

    # selected_rows = frame.iloc[2:5]
    # print(selected_rows)

    # frame = pd.concat([frame, pd.DataFrame(
    #     {
    #         "person_id": 10,
    #         "person_name": "Akram",
    #         "person_city": "Rasht",
    #         "person_age": 45
    #     },
    #     index=[6]
    # )])
    # print(frame)
    #

    # frame = frame.drop_duplicates(subset=["person_age"])
    # print(frame)


if __name__ == "__main__":
    # write_to_file()
    # read_from_file()
    read_from_db()
