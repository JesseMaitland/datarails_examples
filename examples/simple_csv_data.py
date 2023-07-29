import pandas as pd
from datarails.step import DataRailsStep
from datarails.runner import StepRunner


class LoadCarDataFromCSV(DataRailsStep):
    """Loads a CSV file of car data into a pandas DataFrame.

    Inherits from DataRailsStep.
    """

    def step_load_raw_cars_csv(self) -> None:
        """Loads a CSV file of car data into the 'cars' DataFrame.

        The CSV file is assumed to be located at '../data/cars.csv' with ';' as the separator,
        and the first row of the file is used as the header.
        """
        df = pd.read_csv('../data/cars.csv', sep=';', header=0)
        self.dbx.put_df('cars', df)


class FormatDataTypes(DataRailsStep):
    """Formats the data types of a DataFrame.

    Inherits from DataRailsStep. This class is intended to process the 'cars' DataFrame.
    """

    DATA_TYPES = {
        'MPG': "float64",
        'Cylinders': "int64",
        'Displacement': "float64",
        'Horsepower': "float64",
        'Weight': "float64",
        'Acceleration': "float64",
        'Model': "int64",
        'Origin': "string"
    }

    def step_drop_first_row(self) -> None:
        """Removes the first row from the 'cars' DataFrame."""
        self.dbx.cars = self.dbx.cars.iloc[1:]

    def step_set_data_types(self) -> None:
        """Sets the data types for the 'cars' DataFrame.

        The data types to use are specified in the DATA_TYPES class attribute.
        """
        self.dbx.cars = self.dbx.cars.astype(self.DATA_TYPES)


class FindCarWeightOver2000(DataRailsStep):
    """Filters cars that weigh over 2000 from a DataFrame and saves the result in a separate DataFrame.

    Inherits from DataRailsStep. This class is intended to process the 'cars' DataFrame.
    """

    def step_find_weight_over_2000(self) -> None:
        """Filters cars that weigh over 2000 from the 'cars' DataFrame.

        The resulting DataFrame is stored as 'cars_over_2000' in the DataBox.
        """
        df = self.dbx.cars[self.dbx.cars['Weight'] > 2000]
        self.dbx.put_df('cars_over_2000', df)


class SaveDataToCSV(DataRailsStep):
    """Saves a DataFrame to a CSV file.

    Inherits from DataRailsStep. This class is intended to process the 'cars_over_2000' DataFrame.
    """

    def step_save_to_csv(self) -> None:
        """Saves the 'cars_over_2000' DataFrame to a CSV file.

        The CSV file is saved at '../data/processed/cars_over_2000.csv',
        uses ';' as the separator, and does not include the DataFrame's index.
        """
        self.dbx.cars_over_2000.to_csv('../data/processed/cars_over_2000.csv', sep=';', index=False)


steps = [
    LoadCarDataFromCSV,
    FormatDataTypes,
    FindCarWeightOver2000,
    SaveDataToCSV
]

runner = StepRunner(steps=steps)

if __name__ == '__main__':
    runner.run()
