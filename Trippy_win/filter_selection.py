'''
This function contains the filter selection logic for the trippy photo Program
'''
fil = ['color', 'gray', 'gauss','delta','sobel', 'laplace', 'threshold', 'delta_plus', 'blue' ]
fil_dic = {}

def select_filter(filter, status):
    # change required filter to true
    fil_dic = {x:False for x in fil}
    if filter in fil_dic:
        assert type(status) == bool
        fil_dic[filter] = status
    return fil_dic

all_vals = select_filter('gray', True)
print(all_vals['blue'])

all_filters
'''
color = True
gray = False
gauss = False
laplace = False
delta = False
sobel = False
threshold = False

def gray_filter(self):
    self.gray = True
    self.gauss = False
    self.laplace = False
    self.color = False
    self.delta = False
    self.sobel = False
    self.threshold = False
    self.blue = False
    self.delta_plus = False
def delta_filter_plus(self):
    self.color = False
    self.gray = False
    self.gauss = False
    self.laplace = False
    self.delta = False
    self.delta_plus = True
    self.sobelx = False
    self.threshold = False
    self.blue = False
    self.frame_delta_plus = None
def gauss_filter(self):
    self.gray = False
    self.gauss = True
    self.laplace = False
    self.color = False
    self.delta = False
    self.sobel = False
    self.threshold = False
    self.blue = False
    self.delta_plus = False
def delta_filter(self):
    self.gray = False
    self.gauss = False
    self.laplace = False
    self.color = False
    self.delta = True
    self.sobel = False
    self.threshold = False
    self.blue = False
    self.delta_plus = False
def laplace_filter(self):
    self.gray = False
    self.gauss = False
    self.laplace = True
    self.color = False
    self.delta = False
    self.sobel = False
    self.threshold = False
    self.blue = False
    self.delta_plus = False
def threshold_filter(self):
    self.gray = False
    self.gauss = False
    self.laplace = False
    self.color = False
    self.delta = False
    self.sobel = False
    self.threshold = True
    self.blue = False
    self.delta_plus = False
def sobel_filter(self):
    self.gray = False
    self.gauss = False
    self.laplace = False
    self.color = False
    self.delta = False
    self.sobel = True
    self.threshold = False
    self.blue = False
    self.delta_plus = False
def no_filter(self):
    self.gray = False
    self.gauss = False
    self.laplace = False
    self.color = True
    self.delta = False
    self.sobel = False
    self.threshold = False
    self.blue = False
    self.delta_plus = False
def blue_filter(self):
    self.gray = False
    self.gauss = False
    self.laplace = False
    self.color = False
    self.delta = False
    self.sobel = False
    self.threshold = False
    self.blue = True
    self.delta_plus = False
'''
