#################################################################
#					main function relationship
#  				computeweight<----------computeDistance
#				|
#compute<--------
#				|
#				iterpolate<----------computeLineKB
#
#Requirment 1:shapefile which need to be point that transformed by polygon,and the transform rule is 'feature turing point to point'
#			2:shapefile of a polygon
#

import arcpy
import math

#insrc='F:\\Users\\young\\Documents\\ArcGIS\\Default.gdb\\Export_output_5_Project'
insrc=''#location of the shapefile

def getPolygonDetail(infc):
	'''
	get details of the polygon
	'''
	desc = arcpy.Describe(infc)
	shapefieldname = desc.ShapeFieldName
	rows = arcpy.SearchCursor(infc)
	for row in rows:
   	feat = row.getValue(shapefieldname)
    	for part in feat:	
    		with open('temp.txt','w') as f:
    			f.writelines(str(len(part)))

#insrc='E:\\OnTheMove\Data\\Export_Output_149.shp'
def loadData():
  	'''
	get point number of some feature
	'''
	#with open('E:\\OnTheMove\\Data\\temp.txt') as f:
	#	return f.readlines()
	with open('temp.txt') as f:
		return f.readlines()

def getLonLat():
	'''
	get points from shapefile
	'''
	desc=arcpy.Describe(insrc)
	shapefieldname = desc.ShapeFieldName
	rows = arcpy.SearchCursor(insrc)
	points=[]
	for row in rows:
		feat = row.getValue(shapefieldname)
		pnt = feat.getPart()    
		point=[]	
		point.append(pnt.X)
		point.append(pnt.Y) 
		points.append(point)
	return points

def splitor(points,num):	
	'''
	make feature and return a feature list
	'''
	features=[]
	index=0
	for x in num:
		feature=[]
		for y in xrange(int(x)):
			point=[]
			point.append(points[index+y][0])#x
			point.append(points[index+y][1])#y
	 		feature.append(point)		
	 		#print index,x,y	
	 	feature.pop()
		features.append(feature)				
		index+=int(x)		
	#print index
	return features

def interpolate(point1,point2,num):
	'''
	interpolate between two points
	'''
	x=abs(point1[0]-point2[0])
	y=abs(point1[1]-point2[1])
	#print x,y,num
	intervalX=x/num
	intervalY=y/num
	points=[]
	for n in xrange(num):
		point=[]
		point.append(minValue(point1[0],point2[0])+intervalX*n)
		point.append((minValue(point1[0],point2[0])+intervalX*n)*computeLineKB(point1,point2)[0]+computeLineKB(point1,point2)[1])
		points.append(point)
	return points

def minValue(x,y):
	'''
	compare two value
	return the min
	'''
	if x>y:
		return y
	else:
		return x

def computeDistance(point1,point2):
	'''
	return distance between two points
	'''
	return math.sqrt(pow(abs(point1[0]-point2[0]),2)+pow(abs(point1[1]-point2[1]),2))

def computeLineKB(point1,point2):
	'''
	compute k and b of o line
	'''
	k=(point1[0]-point2[0])/(point1[1]-point2[1])
	b=point1[1]-point1[0]*k
	return [k,b]

def computeWeight(feature,pointsNum):
	'''
	compute weight of every edge of a polygon
	'''
	temp=[]	
	for i in xrange(len(feature)):
		if i!=len(feature)-1:
			temp.append(computeDistance(feature[i],feature[i+1]))
		else:		
			temp.append(computeDistance(feature[i],feature[0]))	
	tempSum=reduce(lambda x,y:x+y,temp)	
	return map(lambda x:x*pointsNum/tempSum,temp)
		
def compute(features,pointsNum):	
	'''
	compute desenficated polygon
	'''
	Features=[]
	for feature in features:	
		Feature=[]	
		weight=computeWeight(feature,pointsNum)	
		#print filter(lambda x:x<1,weight)
		for point in xrange(len(feature)-1):						
			Feature.extend(interpolate(feature[point],feature[point+1],int(math.ceil(weight[point]))))
		Features.append(Feature)
	return Features

def lineTest():
	p1=[2,0]
	p2=[1,1]
	#print computeLineKB(p1,p2)
	print computeDistance(p1,p2)

def dataTest():
	num=loadData()	
	count=0
	for x in num:
		count+=int(x)
	print count
	print len(num)
	points=getLonLat()	
	print len(points)

if __name__=='__main__':
	#lineTest()
	num=loadData()
	points=getLonLat()
	print len(points)
	features=splitor(points,num)
	print len(features)
	Features=compute(features,200)
	print len(Features)
	with open('LonLat.txt','w') as f:
		for x in Features:
			for y in x:
				f.writelines('%s    \t%s    \t%s\n'%(len(x),y[0],y[1]))				
	print 'Finished!'
			
	#print features[0]# first feature
	#print features[0][0]#  ff first point
