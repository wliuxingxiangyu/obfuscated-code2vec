from selection_methods import SelectAll
from agg_functions import VectorMean
from arff_file import ARFFFile
from reduction_methods import NoReduction

class AggregationPipeline:

  def __init__(self, model_name, selection_method = SelectAll, agg_function = VectorMean, dim_reduction = NoReduction, output_format = ARFFFile):
    self.model_name = model_name
    self.selection_method = selection_method
    self.agg_function = agg_function
    self.dim_reduction = dim_reduction
    self.output_format = output_format

  def aggregate_vectors(self, vectors):
    if len(vectors) > 0:
      # Select only the vectors we want to select
      selector = self.selection_method(vectors)
      selected_vectors = selector.select()

      # Aggregate them into a single vector
      aggregator = self.agg_function(selected_vectors)
      single_vector = aggregator.aggregate()

      return single_vector
    else:
      return []

  def process_dataset(self, dataset):
    # Reduce the dimensionality of the dataset
    reducer = self.dim_reduction(dataset)
    reduced_dim_dataset = reducer.reduce()

    # Output it in the desired format
    wf = ARFFFile(
        self.model_name, 
        self.selection_method.name(), 
        self.agg_function.name(), 
        self.dim_reduction.name(),
        reduced_dim_dataset)
    wf.write_to_file()




