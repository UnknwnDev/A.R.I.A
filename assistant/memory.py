import json
import datetime


class Memory:
    def __init__(self) -> None:
        self.file_path = "data/memory.json"
        self.current_date = datetime.date.today().strftime("%m/%d/%Y")

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

        with open(self.file_path, "r+") as file:
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
        data = None
        # Open file
        with open(self.file_path, "r") as file:
            # Load existing data
            try:
                file_data = json.load(file)
            except Exception:
                # File is empty
                return None

            # Loads the days current data
            if self.current_date in file_data.keys():
                if _type in file_data[self.current_date].keys():
                    data = file_data[self.current_date][_type]

        # Data found
        return data
