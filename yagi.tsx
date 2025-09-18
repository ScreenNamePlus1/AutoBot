import React, { useState, useMemo } from 'react';
import { Calculator, Radio, Zap, TrendingUp, Settings, Info } from 'lucide-react';

const YagiCalculator = () => {
  const [frequency, setFrequency] = useState('144.5');
  const [numDirectors, setNumDirectors] = useState('3');
  const [wireGauge, setWireGauge] = useState('14');
  const [boomMaterial, setBoomMaterial] = useState('wood');
  const [optimizeFor, setOptimizeFor] = useState('gain');
  const [units, setUnits] = useState('metric');

  // Wire diameter lookup table (in mm)
  const wireGauges = {
    '12': 2.053,
    '14': 1.628,
    '16': 1.291,
    '18': 1.024,
    '20': 0.812
  };

  // Boom correction factors
  const boomCorrections = {
    'wood': 1.0,
    'aluminum': 0.95,
    'fiberglass': 0.98,
    'pvc': 0.97
  };

  const calculations = useMemo(() => {
    const freq = parseFloat(frequency);
    const dirs = parseInt(numDirectors);
    
    if (!freq || freq <= 0 || isNaN(dirs) || dirs < 0) {
      return null;
    }

    const c = 299792458; // speed of light
    const wavelength = c / (freq * 1e6); // wavelength in meters
    const wireDiameter = wireGauges[wireGauge] / 1000; // convert mm to m
    const boomFactor = boomCorrections[boomMaterial];

    // More accurate end effect calculation
    const endEffect = 0.0254 * Math.log10(wavelength / (wireDiameter * 1000));

    // Element calculations with optimization
    let reflectorLength, drivenLength, directorLengths = [];
    let reflectorSpacing, directorSpacings = [];
    let gain, frontToBack, beamwidth;

    if (optimizeFor === 'gain') {
      // Optimized for maximum gain
      reflectorLength = (0.482 * wavelength - endEffect) * boomFactor;
      drivenLength = (0.465 * wavelength - endEffect) * boomFactor;
      reflectorSpacing = 0.15 * wavelength;
      
      // Progressive director sizing for gain optimization
      for (let i = 0; i < dirs; i++) {
        const reduction = 0.005 + (i * 0.003);
        directorLengths.push((0.440 - reduction) * wavelength - endEffect * boomFactor);
        directorSpacings.push(0.15 * wavelength + (i * 0.1 * wavelength));
      }
      
      gain = 8.5 + (dirs * 1.8) - (dirs * 0.1 * dirs); // Diminishing returns
      frontToBack = 15 + (dirs * 2.5);
      beamwidth = Math.max(25, 65 - (dirs * 4));
      
    } else if (optimizeFor === 'bandwidth') {
      // Optimized for wider bandwidth
      reflectorLength = (0.475 * wavelength - endEffect) * boomFactor;
      drivenLength = (0.470 * wavelength - endEffect) * boomFactor;
      reflectorSpacing = 0.125 * wavelength;
      
      for (let i = 0; i < dirs; i++) {
        const reduction = 0.003 + (i * 0.002);
        directorLengths.push((0.445 - reduction) * wavelength - endEffect * boomFactor);
        directorSpacings.push(0.125 * wavelength + (i * 0.08 * wavelength));
      }
      
      gain = 7.8 + (dirs * 1.6) - (dirs * 0.08 * dirs);
      frontToBack = 12 + (dirs * 2.2);
      beamwidth = Math.max(30, 70 - (dirs * 3.5));
      
    } else { // front-to-back ratio
      reflectorLength = (0.490 * wavelength - endEffect) * boomFactor;
      drivenLength = (0.463 * wavelength - endEffect) * boomFactor;
      reflectorSpacing = 0.18 * wavelength;
      
      for (let i = 0; i < dirs; i++) {
        const reduction = 0.007 + (i * 0.004);
        directorLengths.push((0.435 - reduction) * wavelength - endEffect * boomFactor);
        directorSpacings.push(0.16 * wavelength + (i * 0.12 * wavelength));
      }
      
      gain = 7.2 + (dirs * 1.4) - (dirs * 0.06 * dirs);
      frontToBack = 18 + (dirs * 3.2);
      beamwidth = Math.max(28, 72 - (dirs * 4.2));
    }

    // Calculate total boom length
    const totalBoom = reflectorSpacing + (dirs > 0 ? directorSpacings[dirs - 1] : 0);
    
    // Input impedance estimation
    const inputImpedance = 28 + (dirs * 4) + (reflectorSpacing / wavelength * 50);

    return {
      wavelength,
      reflectorLength,
      drivenLength,
      directorLengths,
      reflectorSpacing,
      directorSpacings,
      totalBoom,
      gain: Math.min(gain, 20), // Realistic upper limit
      frontToBack: Math.min(frontToBack, 35),
      beamwidth: Math.max(beamwidth, 15),
      inputImpedance,
      wireDiameter
    };
  }, [frequency, numDirectors, wireGauge, boomMaterial, optimizeFor]);

  const convertLength = (meters) => {
    if (units === 'metric') {
      if (meters < 0.01) return `${(meters * 1000).toFixed(1)} mm`;
      if (meters < 1) return `${(meters * 100).toFixed(1)} cm`;
      return `${meters.toFixed(3)} m`;
    } else {
      const inches = meters * 39.3701;
      if (inches < 12) return `${inches.toFixed(2)}"`;
      const feet = Math.floor(inches / 12);
      const remainingInches = inches % 12;
      return `${feet}' ${remainingInches.toFixed(2)}"`;
    }
  };

  return (
    <div className="max-w-6xl mx-auto p-6 bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen">
      <div className="bg-white rounded-xl shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white p-6">
          <div className="flex items-center gap-3">
            <Radio className="h-8 w-8" />
            <div>
              <h1 className="text-3xl font-bold">Advanced Yagi Antenna Calculator</h1>
              <p className="text-blue-100 mt-1">Professional-grade antenna design tool for amateur radio</p>
            </div>
          </div>
        </div>

        <div className="grid lg:grid-cols-2 gap-8 p-6">
          {/* Input Panel */}
          <div className="space-y-6">
            <div className="bg-gray-50 rounded-lg p-4">
              <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                <Settings className="h-5 w-5" />
                Design Parameters
              </h3>
              
              <div className="grid gap-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Frequency (MHz)
                  </label>
                  <input
                    type="number"
                    step="0.1"
                    value={frequency}
                    onChange={(e) => setFrequency(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    placeholder="144.5"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Number of Directors
                  </label>
                  <input
                    type="number"
                    min="0"
                    max="20"
                    value={numDirectors}
                    onChange={(e) => setNumDirectors(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Wire Gauge (AWG)
                  </label>
                  <select
                    value={wireGauge}
                    onChange={(e) => setWireGauge(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="12">12 AWG (2.05mm)</option>
                    <option value="14">14 AWG (1.63mm)</option>
                    <option value="16">16 AWG (1.29mm)</option>
                    <option value="18">18 AWG (1.02mm)</option>
                    <option value="20">20 AWG (0.81mm)</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Boom Material
                  </label>
                  <select
                    value={boomMaterial}
                    onChange={(e) => setBoomMaterial(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="wood">Wood (Non-conductive)</option>
                    <option value="aluminum">Aluminum</option>
                    <option value="fiberglass">Fiberglass</option>
                    <option value="pvc">PVC</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Optimize For
                  </label>
                  <select
                    value={optimizeFor}
                    onChange={(e) => setOptimizeFor(e.target.value)}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="gain">Maximum Gain</option>
                    <option value="bandwidth">Wide Bandwidth</option>
                    <option value="f2b">Front-to-Back Ratio</option>
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Units
                  </label>
                  <div className="flex gap-2">
                    <button
                      onClick={() => setUnits('metric')}
                      className={`px-3 py-2 rounded-md text-sm font-medium ${
                        units === 'metric' 
                          ? 'bg-blue-600 text-white' 
                          : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                      }`}
                    >
                      Metric
                    </button>
                    <button
                      onClick={() => setUnits('imperial')}
                      className={`px-3 py-2 rounded-md text-sm font-medium ${
                        units === 'imperial' 
                          ? 'bg-blue-600 text-white' 
                          : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                      }`}
                    >
                      Imperial
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Results Panel */}
          <div className="space-y-6">
            {calculations && (
              <>
                {/* Performance Metrics */}
                <div className="bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg p-4 border border-green-200">
                  <h3 className="text-lg font-semibold mb-4 flex items-center gap-2 text-green-800">
                    <TrendingUp className="h-5 w-5" />
                    Estimated Performance
                  </h3>
                  
                  <div className="grid grid-cols-2 gap-4">
                    <div className="text-center">
                      <div className="text-2xl font-bold text-green-700">{calculations.gain.toFixed(1)}</div>
                      <div className="text-sm text-green-600">dBi Gain</div>
                    </div>
                    <div className="text-center">
                      <div className="text-2xl font-bold text-green-700">{calculations.frontToBack.toFixed(1)}</div>
                      <div className="text-sm text-green-600">dB F/B Ratio</div>
                    </div>
                    <div className="text-center">
                      <div className="text-2xl font-bold text-green-700">{calculations.beamwidth.toFixed(0)}°</div>
                      <div className="text-sm text-green-600">Beamwidth</div>
                    </div>
                    <div className="text-center">
                      <div className="text-2xl font-bold text-green-700">{calculations.inputImpedance.toFixed(0)}Ω</div>
                      <div className="text-sm text-green-600">Impedance</div>
                    </div>
                  </div>
                </div>

                {/* Element Dimensions */}
                <div className="bg-gray-50 rounded-lg p-4">
                  <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                    <Calculator className="h-5 w-5" />
                    Element Dimensions
                  </h3>
                  
                  <div className="space-y-3">
                    <div className="flex justify-between items-center p-3 bg-red-100 rounded-md border-l-4 border-red-500">
                      <span className="font-medium">Reflector</span>
                      <span className="font-mono text-sm">{convertLength(calculations.reflectorLength)}</span>
                    </div>
                    
                    <div className="flex justify-between items-center p-3 bg-yellow-100 rounded-md border-l-4 border-yellow-500">
                      <span className="font-medium">Driven Element</span>
                      <span className="font-mono text-sm">{convertLength(calculations.drivenLength)}</span>
                    </div>
                    
                    {calculations.directorLengths.map((length, i) => (
                      <div key={i} className="flex justify-between items-center p-3 bg-blue-100 rounded-md border-l-4 border-blue-500">
                        <span className="font-medium">Director {i + 1}</span>
                        <span className="font-mono text-sm">{convertLength(length)}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Spacing */}
                <div className="bg-gray-50 rounded-lg p-4">
                  <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
                    <Zap className="h-5 w-5" />
                    Element Spacing
                  </h3>
                  
                  <div className="space-y-3">
                    <div className="flex justify-between items-center p-3 bg-purple-100 rounded-md">
                      <span className="font-medium">Reflector ← Driven</span>
                      <span className="font-mono text-sm">{convertLength(calculations.reflectorSpacing)}</span>
                    </div>
                    
                    {calculations.directorSpacings.map((spacing, i) => (
                      <div key={i} className="flex justify-between items-center p-3 bg-purple-100 rounded-md">
                        <span className="font-medium">Driven → Director {i + 1}</span>
                        <span className="font-mono text-sm">{convertLength(spacing)}</span>
                      </div>
                    ))}
                    
                    <div className="flex justify-between items-center p-3 bg-indigo-100 rounded-md border-2 border-indigo-300">
                      <span className="font-bold">Total Boom Length</span>
                      <span className="font-mono text-sm font-bold">{convertLength(calculations.totalBoom)}</span>
                    </div>
                  </div>
                </div>

                {/* Construction Notes */}
                <div className="bg-amber-50 rounded-lg p-4 border border-amber-200">
                  <h4 className="font-semibold mb-2 flex items-center gap-2 text-amber-800">
                    <Info className="h-4 w-4" />
                    Construction Notes
                  </h4>
                  <ul className="text-sm space-y-1 text-amber-700">
                    <li>• Split driven element at center for feed connection</li>
                    <li>• Use a 1:1 balun for best SWR performance</li>
                    <li>• Ensure all elements are parallel and perpendicular to boom</li>
                    <li>• Fine-tune by adjusting element lengths ±2-3%</li>
                    <li>• Consider weatherproofing for outdoor installations</li>
                  </ul>
                </div>
              </>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default YagiCalculator;