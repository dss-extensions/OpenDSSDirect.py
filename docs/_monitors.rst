
Monitors
========


.. automodule:: opendssdirect.Monitors
            :members:
            :undoc-members:
            :show-inheritance:

.. function:: opendssdirect.Monitors.AllNames

    An array of all Monitor names (array of strings).

.. function:: opendssdirect.Monitors.ByteStream

    A byte array containing monitor stream values. Make sure a 'save' is done first (standard solution modes do this automatically).

.. function:: opendssdirect.Monitors.Count

    The number of Monitors.

.. function:: opendssdirect.Monitors.Element

    The full name of element being monitored by the active Monitor.Set the full name of element being monitored by the active Monitor.

.. function:: opendssdirect.Monitors.FileName

    The name of the CSV file associated with active monitor.

.. function:: opendssdirect.Monitors.FileVersion

    The Monitor File version (integer).

.. function:: opendssdirect.Monitors.First

    Set the first monitor active. Returns 0 if no Monitors.

.. function:: opendssdirect.Monitors.Mode

    The monitor mode (bitmask integer - see DSS Help).Set the monitor mode (bitmask integer - see DSS Help).

.. function:: opendssdirect.Monitors.Name

    The active Monitor object by name.Set the active Monitor object by name.

.. function:: opendssdirect.Monitors.Next

    Set the next monitor active. Returns 0 if no more.

.. function:: opendssdirect.Monitors.Process

    Post-process monitor samples taken so far, e.g., Pst for mode = 4.

.. function:: opendssdirect.Monitors.ProcessAll

    Makes that all Monitors post-process the data taken so far.

.. function:: opendssdirect.Monitors.Reset

    Resets the active Monitor object.

.. function:: opendssdirect.Monitors.ResetAll

    Resets all Monitor object.

.. function:: opendssdirect.Monitors.Sample

    Causes active monitor to take a sample.

.. function:: opendssdirect.Monitors.SampleAll

    Causes all Monitors to take a sample of the present state. Returns 0.

.. function:: opendssdirect.Monitors.Save

    Causes active monitor to save its current sample buffer to its monitor stream. Then you can access the Bytestream or channel data. Most standard solution modes do this automatically.

.. function:: opendssdirect.Monitors.SaveAll

    Save all Monitor buffers to their respective file streams. Returns 0.

.. function:: opendssdirect.Monitors.Show

    Converts monitor file into text and displays with text editor.

.. function:: opendssdirect.Monitors.Terminal

    The terminal number of element being monitored.Set the terminal number of element being monitored.

