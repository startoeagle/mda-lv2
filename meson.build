project('mda-lv2', 'cpp')

plugins = [
  'Ambience',
  'Bandisto',
  'BeatBox',
  'Combo',
  'DX10',
  'DeEss',
  'Degrade',
  'Delay',
  'Detune',
  'Dither',
  'DubDelay',
  'Dynamics',
  'EPiano',
  'Image',
  'JX10',
  'Leslie',
  'Limiter',
  'Loudness',
  'MultiBand',
  'Overdrive',
  'Piano',
  'RePsycho',
  'RezFilter',
  'RingMod',
  'RoundPan',
  'Shepard',
  'Splitter',
  'Stereo',
  'SubSynth',
  'TalkBox',
  'TestTone',
  'ThruZero',
  'Tracker',
  'Transient',
  'VocInput',
  'Vocoder',
]
foreach plugin_name : plugins
  plugin_source = 'src/mda' + plugin_name + '.cpp'
  plugin_header = 'src/mda' + plugin_name + '.h'
  plugin_class_name = 'mda' + plugin_name

  shared_library(
    plugin_name,
    [
      plugin_source,
      'lvz/wrapper.cpp',
      'lvz/AudioEffect.hpp',
      'lvz/gendata.cpp',
    ],
    include_directories: ['src', 'lvz'],
    cpp_args: [
      '-DPLUGIN_CLASS=' + plugin_class_name,
      '-DURI_PREFIX="http://moddevices.com/plugins/mda/"',
      '-DPLUGIN_URI_SUFFIX="' + plugin_class_name + '"',
      '-DPLUGIN_HEADER="' + plugin_header + '"',
    ],
    name_prefix: '', # Remove 'lib' prefix
  )

endforeach
