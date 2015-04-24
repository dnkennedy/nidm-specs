#!/usr/bin/env python
''' Definition of constants

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2014
'''

from rdflib import Namespace

PROV = Namespace('http://www.w3.org/ns/prov#')
NIDM = Namespace('http://purl.org/nidash/nidm#')

NIIRI = Namespace('http://iri.nidash.org/')
SPM = Namespace('http://purl.org/nidash/spm#')
FSL = Namespace('http://purl.org/nidash/fsl#')
RDFS = Namespace('http://www.w3.org/2000/01/rdf-schema#')
CRYPTO = Namespace('http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions#')
DCT = Namespace('http://purl.org/dc/terms/')
# This is a workaround to avoid issue with "#" in base prefix as 
# described in https://github.com/RDFLib/rdflib/issues/379,
# When the fix is introduced in rdflib this line will be replaced by:
# OWL = Namespace('http://www.w3.org/2002/07/owl#')
OWL = Namespace('http://www.w3.org/2002/07/owl')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')

OBO_URL = "http://purl.obolibrary.org/obo/"
OBO = Namespace(OBO_URL)

# NIDM constants
FSL_FEAT_VERSION = FSL['FSL_0000005']
FSL_DRIFT_CUTOFF_PERIOD = FSL['FSL_0000004']
FSL_TEMPORAL_DERIVATIVE = FSL['FSL_0000003']
FSL_GAUSSIAN_RUNNING_LINE_DRIFT_MODEL = FSL['FSL_0000002']
FSL_FSLS_GAMMA_DIFFERENCE_HRF = FSL['FSL_0000001']
SPM_SMALLEST_SIGNIFICANT_CLUSTER_SIZE_IN_VOXELS_FWE05 = SPM['SPM_0000014']
SPM_SMALLEST_SIGNIFICANT_CLUSTER_SIZE_IN_VOXELS_FDR05 = SPM['SPM_0000013']
SPM_SMALLEST_SIGNIFICANT_CLUSTER_SIZE_IN_VERTICES_FWE05 = SPM['SPM_0000012']
SPM_SMALLEST_SIGNIFICANT_CLUSTER_SIZE_IN_VERTICES_FDR05 = SPM['SPM_0000011']
SPM_SEARCH_VOLUME_RESELS_GEOMETRY = SPM['SPM_0000010']
SPM_NOISE_FWHM_IN_VOXELS = SPM['SPM_0000009']
SPM_NOISE_FWHM_IN_VERTICES = SPM['SPM_0000008']
SPM_NOISE_FWHM_IN_UNITS = SPM['SPM_0000007']
SPM_TEMPORAL_DERIVATIVE = SPM['SPM_0000006']
SPM_KCONJUNCTION_INFERENCE = SPM['SPM_0000005']
SPM_GAMMA_DIFFERENCE_HRF = SPM['SPM_0000004']
SPM_DISPERSION_DERIVATIVE = SPM['SPM_0000003']
SPM_DCT_DRIFT_MODEL = SPM['SPM_0000002']
SPM_SPMS_DRIFT_CUT_OFF_PERIOD = SPM['SPM_0000001']
NIDM_CLUSTERSIZEINRESELS = NIDM['NIDM_0000156']
NIDM_F_MRI_DESIGN = NIDM['NIDM_0000155']
NIDM_MIXED_DESIGN = NIDM['NIDM_0000154']
NIDM_EVENT_RELATED_DESIGN = NIDM['NIDM_0000153']
NIDM_BLOCK_BASED_DESIGN = NIDM['NIDM_0000152']
NIDM_SINE_BASIS_SET = NIDM['NIDM_0000151']
NIDM_LINEAR_SPLINE_BASIS_SET = NIDM['NIDM_0000150']
NIDM_SEARCH_VOLUME_IN_RESELS = NIDM['NIDM_0000149']
NIDM_RESEL_SIZE_IN_VOXELS = NIDM['NIDM_0000148']
NIDM_HEIGHT_CRITICAL_THRESHOLD_FWE_05 = NIDM['NIDM_0000147']
NIDM_HEIGHT_CRITICAL_THRESHOLD_FDR_05 = NIDM['NIDM_0000146']
NIDM_NOISE_ROUGHNESS_IN_VOXELS = NIDM['NIDM_0000145']
NIDM_RESELS_PER_VOXEL_MAP = NIDM['NIDM_0000144']
NIDM_EXPECTED_NUMBER_OF_VOXELS_PER_CLUSTER = NIDM['NIDM_0000143']
NIDM_EXPECTED_NUMBER_OF_VERTICES_PER_CLUSTER = NIDM['NIDM_0000142']
NIDM_EXPECTED_NUMBER_OF_CLUSTERS = NIDM['NIDM_0000141']
NIDM_CLUSTER_CENTER_OF_GRAVITY = NIDM['NIDM_0000140']
NIDM_COORDINATE_VECTOR_IN_VOXELS = NIDM['NIDM_0000139']
NIDM_HAS_MAXIMUM_INTENSITY_PROJECTION = NIDM['NIDM_0000138']
NIDM_SEARCH_VOLUME_IN_VERTICES = NIDM['NIDM_0000137']
NIDM_SEARCH_VOLUME_IN_UNITS = NIDM['NIDM_0000136']
NIDM_CONTRAST_VARIANCE_MAP = NIDM['NIDM_0000135']
NIDM_WITH_ESTIMATION_METHOD = NIDM['NIDM_0000134']
NIDM_VOXEL_UNITS = NIDM['NIDM_0000133']
NIDM_VOXEL_TO_WORLD_MAPPING = NIDM['NIDM_0000132']
NIDM_VOXEL_SIZE = NIDM['NIDM_0000131']
NIDM_VOXEL6CONNECTED = NIDM['NIDM_0000130']
NIDM_VOXEL26CONNECTED = NIDM['NIDM_0000129']
NIDM_VOXEL18CONNECTED = NIDM['NIDM_0000128']
NIDM_VERSION = NIDM['NIDM_0000127']
NIDM_VARIANCE_SPATIAL_MODEL = NIDM['NIDM_0000126']
NIDM_USER_SPECIFIED_THRESHOLD_TYPE = NIDM['NIDM_0000125']
NIDM_TARGET_INTENSITY = NIDM['NIDM_0000124']
NIDM_STATISTIC_TYPE = NIDM['NIDM_0000123']
NIDM_SOFTWARE_VERSION = NIDM['NIDM_0000122']
NIDM_SEARCH_VOLUME_IN_VOXELS = NIDM['NIDM_0000121']
NIDM_RANDOM_FIELD_STATIONARITY = NIDM['NIDM_0000120']
NIDM_Q_VALUE_FDR = NIDM['NIDM_0000119']
NIDM_PIXEL8CONNECTED = NIDM['NIDM_0000118']
NIDM_PIXEL4CONNECTED = NIDM['NIDM_0000117']
NIDM_P_VALUE_UNCORRECTED = NIDM['NIDM_0000116']
NIDM_P_VALUE_FWER = NIDM['NIDM_0000115']
NIDM_P_VALUE = NIDM['NIDM_0000114']
NIDM_OBJECT_MODEL = NIDM['NIDM_0000113']
NIDM_NUMBER_OF_DIMENSIONS = NIDM['NIDM_0000112']
NIDM_NUMBER_OF_CLUSTERS = NIDM['NIDM_0000111']
NIDM_GAUSSIAN_HRF = NIDM['NIDM_0000110']
NIDM_MIN_DISTANCE_BETWEEN_PEAKS = NIDM['NIDM_0000109']
NIDM_MAX_NUMBER_OF_PEAKS_PER_CLUSTER = NIDM['NIDM_0000108']
NIDM_MASKED_MEDIAN = NIDM['NIDM_0000107']
NIDM_IS_USER_DEFINED = NIDM['NIDM_0000106']
NIDM_IN_WORLD_COORDINATE_SYSTEM = NIDM['NIDM_0000105']
NIDM_IN_COORDINATE_SPACE = NIDM['NIDM_0000104']
NIDM_HAS_MAP_HEADER = NIDM['NIDM_0000103']
NIDM_HAS_HRF_BASIS = NIDM['NIDM_0000102']
NIDM_HAS_ERROR_DISTRIBUTION = NIDM['NIDM_0000101']
NIDM_HAS_ERROR_DEPENDENCE = NIDM['NIDM_0000100']
NIDM_HAS_CONNECTIVITY_CRITERION = NIDM['NIDM_0000099']
NIDM_HAS_CLUSTER_LABELS_MAP = NIDM['NIDM_0000098']
NIDM_HAS_ALTERNATIVE_HYPOTHESIS = NIDM['NIDM_0000097']
NIDM_GRAND_MEAN_SCALING = NIDM['NIDM_0000096']
NIDM_GLOBAL_NULL_DEGREE = NIDM['NIDM_0000095']
NIDM_ERROR_VARIANCE_HOMOGENEOUS = NIDM['NIDM_0000094']
NIDM_ERROR_DEGREES_OF_FREEDOM = NIDM['NIDM_0000093']
NIDM_EQUIVALENT_ZSTATISTIC = NIDM['NIDM_0000092']
NIDM_EFFECT_DEGREES_OF_FREEDOM = NIDM['NIDM_0000091']
NIDM_DIMENSIONS_IN_VOXELS = NIDM['NIDM_0000090']
NIDM_DEPENDENCE_SPATIAL_MODEL = NIDM['NIDM_0000089']
NIDM_HAS_DRIFT_MODEL = NIDM['NIDM_0000088']
NIDM_DRIFT_MODEL = NIDM['NIDM_0000087']
NIDM_COORDINATE_VECTOR = NIDM['NIDM_0000086']
NIDM_CONTRAST_NAME = NIDM['NIDM_0000085']
NIDM_CLUSTER_SIZE_IN_VOXELS = NIDM['NIDM_0000084']
NIDM_CLUSTER_SIZE_IN_VERTICES = NIDM['NIDM_0000083']
NIDM_CLUSTER_LABEL_ID = NIDM['NIDM_0000082']
NIDM_WORLD_COORDINATE_SYSTEM = NIDM['NIDM_0000081']
NIDM_VOXEL_CONNECTIVITY_CRITERION = NIDM['NIDM_0000080']
NIDM_TWO_TAILED_TEST = NIDM['NIDM_0000079']
NIDM_TALAIRACH_COORDINATE_SYSTEM = NIDM['NIDM_0000078']
NIDM_SUBJECT_COORDINATE_SYSTEM = NIDM['NIDM_0000077']
NIDM_STATISTIC_MAP = NIDM['NIDM_0000076']
NIDM_STANDARDIZED_COORDINATE_SYSTEM = NIDM['NIDM_0000075']
NIDM_SPATIALLY_REGULARIZED_MODEL = NIDM['NIDM_0000074']
NIDM_SPATIALLY_LOCAL_MODEL = NIDM['NIDM_0000073']
NIDM_SPATIALLY_GLOBAL_MODEL = NIDM['NIDM_0000072']
NIDM_SPATIAL_MODEL = NIDM['NIDM_0000071']
NIDM_SIGNIFICANT_CLUSTER = NIDM['NIDM_0000070']
NIDM_FOURIER_BASIS_SET = NIDM['NIDM_0000069']
NIDM_SEARCH_SPACE_MASK_MAP = NIDM['NIDM_0000068']
NIDM_CUSTOM_BASIS_SET = NIDM['NIDM_0000067']
NIDM_RESIDUAL_MEAN_SQUARES_MAP = NIDM['NIDM_0000066']
NIDM_POISSON_DISTRIBUTION = NIDM['NIDM_0000065']
NIDM_PIXEL_CONNECTIVITY_CRITERION = NIDM['NIDM_0000064']
NIDM_PEAK_DEFINITION_CRITERIA = NIDM['NIDM_0000063']
NIDM_PEAK = NIDM['NIDM_0000062']
NIDM_PARAMETER_ESTIMATE_MAP = NIDM['NIDM_0000061']
NIDM_ONE_TAILED_TEST = NIDM['NIDM_0000060']
NIDM_NON_PARAMETRIC_SYMMETRIC_DISTRIBUTION = NIDM['NIDM_0000059']
NIDM_NON_PARAMETRIC_DISTRIBUTION = NIDM['NIDM_0000058']
NIDM_NIDM_OBJECT_MODEL = NIDM['NIDM_0000057']
NIDM_MODEL_PARAMETERS_ESTIMATION = NIDM['NIDM_0000056']
NIDM_MNI305_COORDINATE_SYSTEM = NIDM['NIDM_0000055']
NIDM_MASK_MAP = NIDM['NIDM_0000054']
NIDM_MAP_HEADER = NIDM['NIDM_0000053']
NIDM_MAP = NIDM['NIDM_0000052']
NIDM_MNI_COORDINATE_SYSTEM = NIDM['NIDM_0000051']
NIDM_IXI549_COORDINATE_SYSTEM = NIDM['NIDM_0000050']
NIDM_INFERENCE = NIDM['NIDM_0000049']
NIDM_INDEPENDENT_ERROR = NIDM['NIDM_0000048']
NIDM_ICBM_MNI152_NON_LINEAR6TH_GENERATION_COORDINATE_SYSTEM = NIDM['NIDM_0000047']
NIDM_ICBM_MNI152_NON_LINEAR2009C_SYMMETRIC_COORDINATE_SYSTEM = NIDM['NIDM_0000046']
NIDM_ICBM_MNI152_NON_LINEAR2009C_ASYMMETRIC_COORDINATE_SYSTEM = NIDM['NIDM_0000045']
NIDM_ICBM_MNI152_NON_LINEAR2009B_SYMMETRIC_COORDINATE_SYSTEM = NIDM['NIDM_0000044']
NIDM_ICBM_MNI152_NON_LINEAR2009B_ASYMMETRIC_COORDINATE_SYSTEM = NIDM['NIDM_0000043']
NIDM_ICBM_MNI152_NON_LINEAR2009A_SYMMETRIC_COORDINATE_SYSTEM = NIDM['NIDM_0000042']
NIDM_ICBM_MNI152_NON_LINEAR2009A_ASYMMETRIC_COORDINATE_SYSTEM = NIDM['NIDM_0000041']
NIDM_ICBM_MNI152_LINEAR_COORDINATE_SYSTEM = NIDM['NIDM_0000040']
NIDM_ICBM452_WARP5_COORDINATE_SYSTEM = NIDM['NIDM_0000039']
NIDM_ICBM452_AIR_COORDINATE_SYSTEM = NIDM['NIDM_0000038']
NIDM_HEMODYNAMIC_RESPONSE_FUNCTION_DERIVATIVE = NIDM['NIDM_0000037']
NIDM_HEMODYNAMIC_RESPONSE_FUNCTION_BASIS = NIDM['NIDM_0000036']
NIDM_HEMODYNAMIC_RESPONSE_FUNCTION = NIDM['NIDM_0000035']
NIDM_HEIGHT_THRESHOLD = NIDM['NIDM_0000034']
NIDM_GRAND_MEAN_MAP = NIDM['NIDM_0000033']
NIDM_GAUSSIAN_DISTRIBUTION = NIDM['NIDM_0000032']
NIDM_GAMMA_HRF = NIDM['NIDM_0000031']
NIDM_GAMMA_HRB = NIDM['NIDM_0000030']
NIDM_GAMMA_DIFFERENCE_HRF = NIDM['NIDM_0000029']
NIDM_FINITE_IMPULSE_RESPONSE_HRB = NIDM['NIDM_0000028']
NIDM_RESULTS = NIDM['NIDM_0000027']
NIDM_EXTENT_THRESHOLD = NIDM['NIDM_0000026']
NIDM_EXCURSION_SET_MAP = NIDM['NIDM_0000025']
NIDM_EXCHANGEABLE_ERROR = NIDM['NIDM_0000024']
NIDM_ERROR_MODEL = NIDM['NIDM_0000023']
NIDM_ERROR_DISTRIBUTION = NIDM['NIDM_0000022']
NIDM_REGRESSOR_NAMES = NIDM['NIDM_0000021']
NIDM_DISPLAY_MASK_MAP = NIDM['NIDM_0000020']
NIDM_DESIGN_MATRIX = NIDM['NIDM_0000019']
NIDM_DATA = NIDM['NIDM_0000018']
NIDM_CUSTOM_COORDINATE_SYSTEM = NIDM['NIDM_0000017']
NIDM_COORDINATE_SPACE = NIDM['NIDM_0000016']
NIDM_COORDINATE = NIDM['NIDM_0000015']
NIDM_LEGENDRE_POLYNOMIAL_ORDER = NIDM['NIDM_0000014']
NIDM_CONTRAST_STANDARD_ERROR_MAP = NIDM['NIDM_0000013']
NIDM_CONNECTIVITY_CRITERION = NIDM['NIDM_0000012']
NIDM_CONJUNCTION_INFERENCE = NIDM['NIDM_0000011']
NIDM_HAS_FMRI_DESIGN = NIDM['NIDM_0000010']
NIDM_COLIN27_COORDINATE_SYSTEM = NIDM['NIDM_0000009']
NIDM_CLUSTER_LABELS_MAP = NIDM['NIDM_0000008']
NIDM_CLUSTER_DEFINITION_CRITERIA = NIDM['NIDM_0000007']
NIDM_CLUSTER = NIDM['NIDM_0000006']
NIDM_BINOMIAL_DISTRIBUTION = NIDM['NIDM_0000005']
NIDM_BINARY_MAP = NIDM['NIDM_0000004']
NIDM_ARBITRARILY_CORRELATED_ERROR = NIDM['NIDM_0000003']
NIDM_CONTRAST_ESTIMATION = NIDM['NIDM_0000001']
NIDM_CONTRAST_MAP = NIDM['NIDM_0000002']


# OBO constants
OBO_EXAMPLE = OBO['IAO_0000112']
OBO_TERM_EDITOR = OBO['IAO_0000117']
OBO_EDITOR_NOTE = OBO['IAO_0000116']

OBO_PENDING_FINAL = OBO['IAO_0000125']
OBO_METADATA_COMPLETE = OBO['IAO_0000120']
OBO_METADATA_INCOMPLETE = OBO['IAO_0000123']
OBO_REQUIRES_DISCUSSION = OBO['IAO_0000428']
OBO_UNCURATED = OBO['IAO_0000124']
OBO_TO_BE_REPLACED = OBO['IAO_0000423']
OBO_READY = OBO['IAO_0000122']
OBO_DEFINITION = OBO['IAO_0000115']

HAS_CURATION_STATUS = OBO['IAO_0000114']

STATO_OLS = OBO['STATO_0000370']
STATO_OLS_STR = str(STATO_OLS).replace(OBO_URL, "obo:")
# TODO: labels should be grabbed automatically from the corresponding owl file
STATO_OLS_LABEL = "obo:'ordinary least squares estimation'"
STATO_GLS = OBO['STATO_0000372']
STATO_GLS_STR = str(STATO_GLS).replace(OBO_URL, "obo:")
STATO_GLS_LABEL = "obo:'generalized least squares estimation'"
STATO_TSTATISTIC = OBO['STATO_0000176']
STATO_TSTATISTIC_STR = str(STATO_TSTATISTIC).replace(OBO_URL, "obo:")
STATO_TSTATISTIC_LABEL = "obo:'t-statistic'"
STATO_ZSTATISTIC = OBO['STATO_0000376']
STATO_ZSTATISTIC_STR = str(STATO_ZSTATISTIC).replace(OBO_URL, "obo:")
STATO_ZSTATISTIC_LABEL = "obo:'Z-statistic'"
STATO_CONTRAST_WEIGHT_MATRIX = OBO['STATO_0000323']



