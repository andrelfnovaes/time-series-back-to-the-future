import numpy as np
import pandas as pd

class TimeSeries:
    """
    A class for representing and manipulating time series data.

    Attributes:
    -----------
    data : pd.Series
        The time series data.
    name : str
        Name or label for the time series.
    """

    def __init__(self, data: pd.Series, name: str = "Unnamed Series"):
        """
        Initializes the TimeSeries object with time series data.

        Parameters:
        ----------
        data : pd.Series
            A pandas Series representing the time series.
        name : str, optional
            The name of the time series, default is 'Unnamed Series'.
        """
        self._validate_input_data(data)
        self._data = data
        self._name = name

    # Encapsulation: Getters and Setters
    @property
    def data(self):
        """Gets the time series data."""
        return self._data

    @data.setter
    def data(self, new_data: pd.Series):
        """Sets the time series data after validation."""
        self._validate_input_data(new_data)
        self._data = new_data

    @property
    def name(self):
        """Gets the name of the time series."""
        return self._name

    @name.setter
    def name(self, new_name: str):
        """Sets the name of the time series."""
        self._name = new_name

    # Method to validate the data input
    def _validate_input_data(self, data):
        if not isinstance(data, pd.Series):
            raise TypeError("Time series data must be a pandas Series.")

    # Methods to manipulate the time series
    def get_summary(self):
        """
        Returns a summary of the time series data.

        Returns:
        -------
        dict
            A dictionary with basic statistics about the time series.
        """
        return {
            'mean': self._data.mean(),
            'median': self._data.median(),
            'std': self._data.std(),
            'min': self._data.min(),
            'max': self._data.max(),
            'length': len(self._data)
        }

    def add_value(self, timestamp, value):
        """
        Adds a new value to the time series.

        Parameters:
        ----------
        timestamp : any
            The timestamp/index for the new value.
        value : float
            The value to add to the time series.
        """
        self._data[timestamp] = value

    def plot(self):
        """
        Plots the time series data.
        """
        import matplotlib.pyplot as plt
        self._data.plot(title=self._name)
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.show()

    # String representation of the object
    def __repr__(self):
        return f"TimeSeries(name='{self._name}', length={len(self._data)})"

    def __str__(self):
        return f"TimeSeries: {self._name}, Length: {len(self._data)}"


# Example Usage
if __name__ == "__main__":
    # Create sample time series data
    dates = pd.date_range('2023-01-01', periods=100)
    values = np.random.randn(100)
    ts_data = pd.Series(values, index=dates)

    # Create a TimeSeries object
    ts = TimeSeries(ts_data, name="Sample Series")

    # Accessing attributes
    print(ts.name)
    print(ts.get_summary())

    # Plot the time series
    ts.plot()

    # Add a new value to the time series
    ts.add_value(pd.Timestamp('2023-04-11'), 1.5)
    print(ts.get_summary())
