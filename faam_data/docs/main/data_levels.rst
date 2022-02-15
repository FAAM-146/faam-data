===========
Data Levels
===========

.. note::

    The information here is adapted from FAAM document `FAAM000002`. It is 
    currently under review and should be expected to change in version 1 of 
    this standard.

Level 00
--------

Unadulterated instrument data in the original file format. File/s may be
compressed as discussed in section 5.

Level 0
-------

Unprocessed instrument data at original resolution. Data may be filtered
to remove any communication artefacts (eg synchronisation markers, dropouts,
or duplicates). Periods of instrument calibration and pre- and post-
flight tails may be removed or flagged. Any filtering is based on instrument-
level quality control.

Level 1A
--------

Geophysical units derived from level 00 or 0 data. Derivations may
utilise Level 1A data or above from other instruments. Nominal or manufacturer's
calibration information has been applied to convert raw data into
level 1A physical units. An 'intermediate' level of quality control has been
applied, see section 3.

Level 1B
--------

Geophysical units derived from level 0 data. Derivations may utilise
Level 1B data or above from other instruments. Verified and traceable
calibration data has been applied to convert raw data into level 1B physical
units. 'Intermediate' quality assurance procedures have been applied.

Level 2A
--------

Level 1A geophysical data averaged or interpolated and/or corrected
for non-standard conditions. For example, sample air flow may be converted
to standard temperature and pressure. An 'intermediate' level of quality
control has been applied.

Level 2B
--------

Level 1B geophysical data averaged or interpolated and/or corrected for
non-standard conditions. For example, sample air flow may be converted
to standard temperature and pressure. An 'intermediate' level of quality
control has been applied.

Level 3
-------

Geophysical variables derived from level 2 data from multiple instruments and/or
flights. A 'comprehensive' level of quality assurance, has been applied.

