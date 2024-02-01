Upgrading to OpenDSSDirect.py v0.9+
===================================

If you are using older OpenDSSDirect.py versions, some specifics changed in v0.9 are important to note. For general changes of the DSS engine, please see the changelog at https://github.com/dss-extensions/dss_capi/blob/master/docs/changelog.md#version-0140

Basic usage of ODD.py can continue as in previous versions, and should mostly keep working out-of-the-box if you do not intend to use multiple DSS instances.
There are also a couple of deprecation warnings introduced to signal some changes to the users.

- Instead of using `import opendssdirect as odd`, we now recommend `from opendssdirect import dss as odd`. This will import a class instance, which exposes more features. For example, the main class (`OpenDSSDirect`) exposes the `OpenDSSDirect.Text.Commands` as the call operator -- you can use `odd('redirect some_script.dss')`, even with multi-line strings.
- The classes also handle a common mistake of new users, which is using OpenDSSDirect.py as DSS-Python or the COM API, accidentally replacing the functions/methods with the indented values instead. That is, something like `from opendssdirect import dss as odd; odd.Text.Command = 'clear'` now results in an error.
- The old `Iterator` class is deprecated since all iterable classes should now support the native iterator protocol in Python. That is `[load.kW() for load in odd.Loads]` now works. Limitations from OpenDSS still applies (a single object of a certain type must be active, etc.).
- `opendssdirect.run_command` is also deprecated due to the lack of direct error handling. We noticed this was resulting in error being ignored by many users, especially new users. 
- Multiple DSS engines are now supported, including multi-threading in Python. This means that some old usage patterns are not recommended anymore, since the code moved from plain modules to classes in order to allow this kind of feature.

.. code-block::python

    from opendssdirect import dss as odd_default

    # When using multiple contexts, it's better avoid changing the 
    # working directory of the process
    odd_default.Basic.AllowChangeDir(False)

    odd1 = odd_default.NewContext()
    odd2 = odd_default.NewContext()

    odd1('new circuit.circuit1')
    odd2('new circuit.circuit2')

    assert odd1.Circuit.Name() == 'circuit1'
    assert odd2.Circuit.Name() == 'circuit2'


- The package now has the option of returning NumPy arrays (like DSS-Python) instead of plain lists. As of v0.9, this is not enabled by default, but it could be in future versions (feedback is welcome). To enable it globally, you can set the environment variable `OPENDSSDIRECT_PY_USE_NUMPY=1`. To enable it on a per-instance base, you can pass `prefer_lists=False` to the constructor. For example, from one of the tests:

.. code-block::python

    from opendssdirect.OpenDSSDirect import OpenDSSDirect
    from numpy import ndarray

    # NOTE: this constructors ALWAYS binds to the default DSS engine.
    odd_np = OpenDSSDirect(prefer_lists=False)
    # Use it normally
    odd_np(f"Redirect '{PATH_TO_DSS}'")
    assert isinstance(odd_np.Circuit.AllBusMagPu(), ndarray)

    odd_lst = OpenDSSDirect(prefer_lists=True)
    # Same global instance, we can just reuse the result
    assert isinstance(odd_lst.Circuit.AllBusMagPu(), list)


- Due to changes in the AltDSS/DSS C-API engine, the capitalization of the DSS property was changed. OpenDSS is case insensitive, but a lot of code assumes a certain capitalization. This is not recommended since OpenDSS already changed the capitalization in the past. Code that relied on the capitalization before should stop working, but we added a way to toggle the capitalization style through `Settings.SetPropertyNameStyle`, as in the snippet below. We'd recommend using this but updating any related code to not depend on the capitalization at all.

.. code-block::python

    from opendssdirect import dss as odd, enums as dss_enums
    odd.Settings.SetPropertyNameStyle(dss_enums.DSSPropertyNameStyle.Legacy)

