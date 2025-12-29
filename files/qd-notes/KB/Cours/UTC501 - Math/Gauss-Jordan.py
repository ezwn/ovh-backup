from fractions import Fraction

def gj(mat):
    LCNT = len(mat)
    CCNT = len(mat[0])

    targ_lin=0
    for icol in range(0, CCNT):
        if targ_lin < LCNT:

            piv_lin = targ_lin
            piv_val = mat[targ_lin][icol]
            for ilin in range(targ_lin, LCNT):
                if abs(mat[ilin][icol]) > abs(piv_val):
                    piv_val = mat[ilin][icol]
                    piv_lin = ilin
            
            if piv_val != 0:
                for c in range(CCNT):
                    mat[piv_lin][c] = Fraction(mat[piv_lin][c], piv_val)

                if piv_lin != targ_lin:
                    mat[piv_lin], mat[targ_lin] = mat[targ_lin], mat[piv_lin]

                for ilin in range(0, LCNT):
                    if ilin != targ_lin:
                        val = mat[ilin][icol]
                        for c in range(CCNT):
                            mat[ilin][c] = mat[ilin][c] - val * mat[targ_lin][c]

                targ_lin = targ_lin + 1
