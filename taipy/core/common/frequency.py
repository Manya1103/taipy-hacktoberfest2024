from taipy.core.common._repr_enum import _ReprEnum


class Frequency(_ReprEnum):
    """Frequency of the recurrence of `Cycle^` and `Scenario^` objects.

    The frequency must be provided in the `ScenarioConfig^`.

    Each recurrent scenario is attached to the cycle corresponding to the creation date and the
    frequency. In other words, each cycle represents an iteration and contains the various scenarios
    created during this iteration.

    For instance, when scenarios have a _MONTHLY_ frequency, one cycle will be created for each
    month (January, February, March, etc.). A new scenario created on February 10th, gets
    attached to the _February_ cycle.

    The frequency is implemented as an enumeration with the following possible values:

    - With a _DAILY_ frequency, a new cycle is created for each day.

    - With a _WEEKLY_ frequency, a new cycle is created for each week (from Monday to Sunday).

    - With a _MONTHLY_ frequency, a new cycle is created for each month.

    - With a _QUARTERLY_ frequency, a new cycle is created for each quarter.

    - With a _YEARLY_ frequency, a new cycle is created for each year.
    """

    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    QUARTERLY = 4
    YEARLY = 5
