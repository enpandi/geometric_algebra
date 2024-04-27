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
match n:
    case 3:
        name = 'pga3d'
        descriptor = ';'.join([
            f'{name}:0,1,1,1',
            'Point:e123,e230,e301,e012',
            'IdealPoint:e230,e301,e012',
            'Line:e01,e02,e03|e23,e31,e12',
            'Scalar:1',
            #'Rotor:1,e23,-e13,e12',
            #'Point:e123,-e023,e013,-e012',
            #'IdealPoint:e01,e02,e03',
            #'Plane:e0,e1,e2,e3',
            #'Line:e01,e02,e03|e23,-e13,e12',
            #'Translator:1,e01,e02,e03',
            #'Motor:1,e23,-e13,e12|e0123,e01,e02,e03',
        ])
    case 4:
        assert False
        name = 'pga4d'
        descriptor = ';'.join([
            f'{name}:0,1,1,1,1',
            'Scalar:1',
            'Rotor:1,e23,-e13,e12',
            'Point:e123,-e023,e013,-e012',
            'IdealPoint:e01,e02,e03',
            'Plane:e0,e1,e2,e3',
            'Line:e01,e02,e03|e23,-e13,e12',
            'Translator:1,e01,e02,e03',
            'Motor:1,e23,-e13,e12|e0123,e01,e02,e03',
        ])
print(descriptor)
import subprocess
subprocess.run(['cargo', 'run', '--', descriptor])