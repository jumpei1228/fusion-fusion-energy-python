"""
核融合の放出エネルギーをPythonで計算する｜E=mc²と質量欠損

元記事: https://fusion.yurufuwa.work/learn/fusion-energy-python
ゆるふわ核融合・次世代エネルギー (fusion.yurufuwa.work) の解説記事から抜粋したコードです。
"""

import numpy as np

# 各粒子の質量 [u（原子質量単位）]
m_D  = 2.014102    # 重水素
m_T  = 3.016049    # 三重水素
m_He = 4.002602    # ヘリウム4
m_n  = 1.008665    # 中性子

mass_before = m_D + m_T
mass_after  = m_He + m_n
defect = mass_before - mass_after           # 質量欠損 [u]

# 1u = 931.494 MeV/c²（E=mc²の換算）
energy_MeV = defect * 931.494
print(f"質量欠損: {defect:.6f} u")
print(f"放出エネルギー: {energy_MeV:.2f} MeV")

# 中性子とHeに分配されるが、反応1回あたりの総エネルギーで概算
J_per_MeV = 1.602e-13
avogadro = 6.022e23
mol_mass = 5.0                # D+Tでおよそ5 g/mol

reactions_per_gram = avogadro / mol_mass
energy_per_gram_J = reactions_per_gram * energy_MeV * J_per_MeV
print(f"1gあたり: {energy_per_gram_J:.2e} J")
print(f"= 石油換算 約 {energy_per_gram_J/4.2e10*1000:.0f} kg 相当")
