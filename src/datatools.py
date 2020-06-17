import numpy as np
from numpy import loadtxt
import torch

def load_dataset(start = 1, end = 2):
	data = np.array((loadtxt("../data/data_" + str(start) +  "_2f_sq.csv", delimiter=',')))
	for i in range(start+1,end+1):
	    new_data = np.array((loadtxt("../data/data_"+str(i)+"_2f_sq.csv", delimiter=',')))
	    data = np.concatenate((data, new_data), axis=0)

	vids = np.array((loadtxt("../data/vids_" + str(start) +  "_2f_sq.csv", delimiter=',')))
	for i in range(start+1,end+1):
	    new_data = np.array((loadtxt("../data/vids_"+str(i)+"_2f_sq.csv", delimiter=',')))
	    vids = np.concatenate((vids, new_data), axis=0)

	return data, vids

def load_dataset_block():
	data = np.array((loadtxt("../data/bdata_" + str(start) +  "_2f_sq.csv", delimiter=',')))
	vids = np.array((loadtxt("../data/bvids_" + str(start) +  "_2f_sq.csv", delimiter=',')))
	
	return data, vids

def parse_data(data, img_dim = 2500, extra_zeros = 160):
	inputs_1 = torch.tensor(data[:,:45]) # object trajectory
	inputs_2 = torch.tensor(data[:,45:205]) # trajectory decoding
	inputs_img = torch.tensor(data[:,205:205+img_dim]) # object shape
	SDF = torch.tensor(data[:,205+img_dim:205+2*img_dim]) # object sdf
	N_data = np.shape(data)[0]
	inputs_2[:,0:20] = torch.tensor(data[:,205+2*img_dim:225+2*img_dim])
	labels = 330*torch.cat((torch.tensor(data[:,205+2*img_dim:]),torch.tensor(np.zeros((N_data,extra_zeros)))), axis = 1)

	return inputs_1, inputs_2, inputs_img, SDF, labels


def parse_dataVids(data, img_dim = 2500, extra_zeros = 160):
	inputs_1 = torch.tensor(data[:,:45]) # object trajectory
	inputs_2 = torch.tensor(data[:,45:205]) # trajectory decoding
	inputs_img = torch.tensor(data[:,205:205+img_dim]) # object shape
	SDF = torch.tensor(data[:,205+img_dim:205+2*img_dim]) # object sdf
	N_data = np.shape(data)[0]
	inputs_2[:,0:20] = torch.tensor(data[:,205+2*img_dim:225+2*img_dim])
	labels = 330*torch.tensor(data[:,205+2*img_dim:])

	return inputs_1, inputs_2, inputs_img, SDF, labels