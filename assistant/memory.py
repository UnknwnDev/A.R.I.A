import json
from datetime import date, datetime, timedelta


class Memory:
    def __init__(self, num_days: int = 5) -> None:
        self.file_path = "data/memory.json"
        self.current_date = date.today().strftime("%m/%d/%Y")
        self.day_span = num_days

    def store_data(self, data=None, _type: str = "conversation") -> int:
        """Stores data generated or created into a json file

        Args:
            data (any, optional): info being stored. Defaults to None.
            _type (str, optional): data type for recall. Defaults to "conversation".

        Returns:
            int: error flag
        """
        if data is None:
            return -1

        with open(self.file_path, "+r") as file:
            # Format

            # Load existing data
            try:
                file_data = json.load(file)
            except Exception:
                # File empty
                file_data = {}

            if self.current_date in file_data.keys():
                if _type in file_data[self.current_date].keys():
                    # print(f"Found {type} in {self.current_date}.")
                    if type(file_data[self.current_date][_type]) is list:
                        file_data[self.current_date][_type].extend(data[:])
                    else:
                        file_data[self.current_date][_type].update(data[:])

                    file.seek(0)
                else:
                    file_data[self.current_date] = {_type: data}
            else:
                file_data.update({self.current_date: {_type: data}})
                file.seek(0)

            json.dump(file_data, file, indent=2)

            # Save the data to a file

        # Data stored correctly
        return 0

    def load_data(self, _type: str = "conversation"):
        """Loads data with given type from json file.

        Args:
            _type (str, optional): data type for recall. Defaults to "conversation".

        Returns:
            any: data found from given data type.
        """

        # Open file
        try:
            with open(self.file_path, "r") as file:
                # Load existing data
                try:
                    file_data = json.load(file)
                except Exception:
                    # File is empty
                    return None

                data = []

                # Gets the previous depending on day span
                days = self.__get_days()

                # Loads the data from days given
                for day in days:
                    if day in file_data.keys():
                        if _type in file_data[day].keys():
                            data.extend(file_data[day][_type])

            # Data found
            return data
        except Exception as e:
            print(e)
            return None

    def __get_days(self) -> list:
        """Creates a list of days previous to current from given day span.

        Returns:
            list: list of days
        """
        today = datetime.now()

        days = []
        for i in range(self.day_span - 1, 0, -1):
            previous_day = today - timedelta(days=i)
            days.append(previous_day.strftime("%m/%d/%Y"))

        days.append(self.current_date)
        return days
