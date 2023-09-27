from test_module import *
import sys

#F:\PythonProjects\project_blender_test\output
output_path=input('Insert path to output directory: ')
x_resolution=eval(input('Insert x render resolution: '))
y_resolution=eval(input('Insert y render resolution: '))

p=Blender_Test()

cube_test_renders_output=f'{output_path}\cube_render_results'
sphere_test_renders_output=f'{output_path}\sphere_render_results'
night_sphere_test_renders_output=f'{output_path}\sphere_night_render_results'

p.create_cube_test(cube_test_renders_output,x_resolution,y_resolution)
p.create_sphere_test_basic_light(sphere_test_renders_output,x_resolution,y_resolution)
p.create_sphere_test_night_light(night_sphere_test_renders_output,x_resolution,y_resolution)