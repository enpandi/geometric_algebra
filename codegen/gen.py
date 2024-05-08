"""
"epga1d:1,1;Scalar:1;ComplexNumber:1,e01"
"epga2d:1,1,1;Scalar:1;MultiVector:1,e12,e1,e2|e0,e012,e01,-e02;Rotor:1,e12;Point:e12,e01,-e02;IdealPoint:e01,-e02;Plane:e0,e2,e1;Translator:1,e01,-e02;Motor:1,e12,e01,-e02;MotorDual:e012,e0,e2,e1"
"epga3d:1,1,1,1;Scalar:1;MultiVector:1,e23,-e13,e12|e0,-e023,e013,-e012|e123,e1,e2,e3|e0123,e01,e02,e03;Rotor:1,e23,-e13,e12;Point:e123,-e023,e013,-e012;IdealPoint:e01,e02,e03;Plane:e0,e1,e2,e3;Line:e01,e02,e03|e23,-e13,e12;Translator:1,e01,e02,e03;Motor:1,e23,-e13,e12|e0123,e01,e02,e03;PointAndPlane:e123,-e023,e013,-e012|e0,e1,e2,e3"

"ppga1d:0,1;Scalar:1;DualNumber:1,e01"
"ppga2d:0,1,1;Scalar:1;MultiVector:1,e12,e1,e2|e0,e012,e01,-e02;Rotor:1,e12;Point:e12,e01,-e02;IdealPoint:e01,-e02;Plane:e0,e2,e1;Translator:1,e01,-e02;Motor:1,e12,e01,-e02;MotorDual:e012,e0,e2,e1"
"ppga3d:0,1,1,1;Scalar:1;MultiVector:1,e23,-e13,e12|e0,-e023,e013,-e012|e123,e1,e2,e3|e0123,e01,e02,e03;Rotor:1,e23,-e13,e12;Point:e123,-e023,e013,-e012;IdealPoint:e01,e02,e03;Plane:e0,e1,e2,e3;Line:e01,e02,e03|e23,-e13,e12;Translator:1,e01,e02,e03;Motor:1,e23,-e13,e12|e0123,e01,e02,e03;PointAndPlane:e123,-e023,e013,-e012|e0,e1,e2,e3"

"hpga1d:-1,1;Scalar:1;SplitComplexNumber:1,e01"
"hpga2d:-1,1,1;Scalar:1;MultiVector:1,e12,e1,e2|e0,e012,e01,-e02;Rotor:1,e12;Point:e12,e01,-e02;IdealPoint:e01,-e02;Plane:e0,e2,e1;Translator:1,e01,-e02;Motor:1,e12,e01,-e02;MotorDual:e012,e0,e2,e1"
"hpga3d:-1,1,1,1;Scalar:1;MultiVector:1,e23,-e13,e12|e0,-e023,e013,-e012|e123,e1,e2,e3|e0123,e01,e02,e03;Rotor:1,e23,-e13,e12;Point:e123,-e023,e013,-e012;IdealPoint:e01,e02,e03;Plane:e0,e1,e2,e3;Line:e01,e02,e03|e23,-e13,e12;Translator:1,e01,e02,e03;Motor:1,e23,-e13,e12|e0123,e01,e02,e03;PointAndPlane:e123,-e023,e013,-e012|e0,e1,e2,e3"
"""

n = 3
if True:
        name = 'pga3d'
        # the generator code is buggy; ensure no isolated elements unless scalar
        # the ones that get sent to the shader have to be formatted flexibly
        descriptor3 = ';'.join([
            f'{name}:0,1,1,1',
            'Scalar:1',
            'Point:-e023,e013,-e012|e123',
            'MeetJoinLine:e01,e02,e03|e23,-e13,e12', # do not instantiate lines directly. alias meet lines and join lines.
            'Motor:e01,e02,e03|e23,-e13,e12|e0123,1',
            'Plane:e1,e2,e3|e0',
            'Rotor:e23,-e13,e12|1',
            'Translator:e01,e02,e03|1',
            'OddVector:e1,e2,e3|-e023,e031,-e012|e123,e0', # required for some intermediate operations
            'MultiVector:1,e23,-e13,e12|e0,-e023,e013,-e012|e123,e1,e2,e3|e0123,e01,e02,e03', # required for some intermediate operations
        ])
        name = 'pga4d'
        descriptor4 = ';'.join([
            f'{name}:0,1,1,1,1',
            'Scalar:1',
            'Point:-e0234,e0134,-e0124,e0123|e1234',
            'JoinLine:-e234,e134,-e124,e123|-e014,-e024,-e034|-e023,e013,-e012',
            'MeetLine:e01,e02,e03,e04|e23,-e13,e12|e14,e24,e34',
            'Motor:e01,e02,e03,e04|e23,-e13,e12|e14,e24,e34|-e0234,e0134,-e0124,e0123|e1234,1',
            'Plane:e1,e2,e3,e4|e0',
            # the ones that get sent to the shader have to be formatted flexibly
            'Rotor:e23,-e13,e12|e14,e24,e34|e1234,1',
            'Translator:e01,e02,e03,e04|1',
            'OddVector:e1,e2,e3,e4|-e234,e134,-e124,e123|-e014,-e024,-e034|-e023,e013,-e012|e01234,e0', # required for various operations(?)
            'MultiVector:e01,e02,e03,e04|e23,-e13,e12|e14,e24,e34|-e0234,e0134,-e0124,e0123|e1234,1|e1,e2,e3,e4|-e234,e134,-e124,e123|-e014,-e024,-e034|-e023,e013,-e012|e01234,e0',
            # required for various operations(?)
        ])
        # https://stackoverflow.com/a/49031090
print(descriptor3)
print(descriptor4)
import subprocess
subprocess.run(['cargo', 'run', '--', descriptor3])
subprocess.run(['cargo', 'run', '--', descriptor4])
