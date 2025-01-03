Concentration-Response Fitting
=====================


Steps
-----

1. **Prepare Concentration-Response Data**: Start with an instance of `CauseEffectData`, containing concentration and survival data for the main stressor.
2. **Configure Settings**: Customize the fit by specifying `CRF_SETTINGS`
3. **Run the Fit**: Call `concentration_response_fit`. The function returns `ConcentrationResponsePrediction`, giving you survival and stress curves, predicted survival values, and lethal concentration metrics.

Classes and Functions
---------------------

Below are the primary classes and functions used for concentration-response fitting.

Concentration Response Fit Settings
--------------------------

.. autoclass:: sam.CRF_SETTINGS
   :members:
   :undoc-members:
   :show-inheritance:
Model Predictions
-----------------

.. autoclass:: sam.ConcentrationResponsePrediction
   :members:
   :undoc-members:
   :show-inheritance:

Concentration Response Fit Function
--------------------------

.. autofunction:: sam.concentration_response_fit

Example Usage
-------------

Here’s how to use `concentration_response_fit` with sample data and custom settings:


.. code-block:: python

   from sam import concentration_response_fit, CRF_SETTINGS, CauseEffectData

   # Sample concentration-response data
   data = CauseEffectData(concentration=[0, 0.5, 1.0, 5.0], survival_rate=[100, 90, 75, 20], name = "example")

   # Custom settings (optional)
   cfg = CRF_SETTINGS(max_survival=100)

   # Perform concentration-response fit
   predictions = concentration_response_fit(data, cfg)

   # Access the model predictions
   print(predictions.survival_curve)