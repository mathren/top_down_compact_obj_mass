# Masses of compact remnant  from CO core masses
__author__ = "M. Renzo (mrenzo@flatironinstitute.org)"

# for fit
import numpy as np
import scipy
from scipy.optimize import curve_fit
# for plot
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


def linear(x, a, b):
    return a*x+b

def fitting_func_Z(data, a, b, c, d):
    """
    shifted cube plus square term, with the coefficient of the cubic
    term linear function in log10(Z)
    """
    mco = data[0]
    Z = data[1]
    return linear(np.log10(Z),a,b)*(mco+c)**3+d*(mco+c)**2

def get_select_datafile_range(datafile):
    """
    datafile1.txt is at https://zenodo.org/record/3346593
    from datafile1.txt selects only the runs with varying Z, ignores
    other parameter variations.
    """
    header_length = 43 # counting from 0
    data_length = 224
    col = ["Z", "Mhe_init", "Mhe_preCC", "Mco", "Mbh", "dMpulse", "dMwind", "dMSN"]
    src = np.zeros([data_length+1, len(col)])
    with open(datafile, 'r') as df:
        for i, line in enumerate(df):
            if (i >= header_length) and (i<= data_length+header_length):
                # print(line.split()[1:-1])
                src[i-header_length,:]=np.array(line.split()[1:-1], dtype=float)
            if i >= data_length+header_length:
                break
    return src, col

if __name__ == "__main__":
    # this gets downloaded from zenodo by showyourwork
    datafile = "../data/datafile1.txt"
    src, col = get_select_datafile_range(datafile)

    fig=plt.figure(figsize=(12,20))
    gs = gridspec.GridSpec(7, 1)
    gs.update(wspace=0.00, hspace=0.00)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    ax3 = fig.add_subplot(gs[2])
    ax4 = fig.add_subplot(gs[3])
    ax5 = fig.add_subplot(gs[4])
    ax6 = fig.add_subplot(gs[5])
    ax7 = fig.add_subplot(gs[6])
    axes = [ax1,ax2,ax3,ax4,ax5,ax6,ax7]
    rainbow = plt.cm.rainbow(np.linspace(0,1,len(axes)))

    # for ax in axes:
    #     ax.scatter(np.linspace(0,1,10), np.linspace(0,1,10), s=1e2*np.linspace(0,1,10), color=rainbow[axes.index(ax)])

    # # --------------------------------------------------------------------------------------
    # fit happens here!
    # load data
    Mco = src[:, col.index("Mco")]
    Z = src[:, col.index('Z')]
    # Mhe = src[:, col.index('Mhe')]
    dMpulse = src[:, col.index('dMpulse')]
    # fit only in the PPISN range -- neglect the Z dependence of this range itself
    ind_for_fit = (Mco>=38) & (Mco<=60)
    popt, pcov = curve_fit(fitting_func_Z, [Mco[ind_for_fit], Z[ind_for_fit]], dMpulse[ind_for_fit])
    # print(popt)
    fit = "$\Delta M_\mathrm{PPI} = ("+f"{popt[0]:.4f}"+r"\log_{10}(Z)+"+f"{popt[1]:.4f})"+r"\times (M_\mathrm{CO}+"+f"{popt[2]:.1f}"+")^3"+f"{popt[3]:.4f}"+r"\times (M_\mathrm{CO}+"+f"{popt[2]:.1f}"+")^2$"
    ax1.set_title(fit, fontsize=20)
    # # --------------------------------------------------------------------------------------

    for i, metallicity in enumerate(sorted(np.unique(Z))):
        ax = axes[i]
        ax.axhline(0, 0,1,lw='1', c='k', ls='--', zorder=0)
        # first plot data
        x = Mco[Z==metallicity]
        y = dMpulse[Z==metallicity]
        ax.scatter(x, y, color=rainbow[i], label=r"$Z="+f"{metallicity:.0e}"+"$")
        # then plot fit
        ind_for_fit = (x>=38) & (x<=60)
        x = x[ind_for_fit]
        ax.plot(x, fitting_func_Z([x,[metallicity]*len(x)],*popt), c=rainbow[i])
        # larger range to show the fit
        xx = np.linspace(30,60,1000)
        yy = fitting_func_Z([xx,[metallicity]*len(xx)],*popt)
        ax.plot(xx, yy, c=rainbow[i], ls="--", lw=8, alpha=0.5, zorder=0)
        # ----------
        ax.legend(fontsize=20, handletextpad=0.1, frameon=True)
        ax.set_ylim(-5,55)
        ax.set_xlim(30,75)
        if ax != ax7:
            ax.set_xticklabels([])


    ax4.set_ylabel(r"$\Delta M_\mathrm{PPI} \ [M_\odot]$")
    ax7.set_xlabel(r"$M_\mathrm{CO} \ [M_\odot]$")

    plt.savefig('./fit_DM_PPI.pdf')
