# Linear Algebra
## Determinant

If determnant is zero, it means there are no solution for a polynomial

det(A) = $ \sum_{\sigma \in S_n}{} sgn(\sigma)\prod_{i=1}^{n}a_i,\sigma(i) $


1. 2 x 2
$$
det(A) = |A| =
\begin{vmatrix}
3&4 \\
6&3
\end{vmatrix}
= 3*3-4*6 = 9-24 = -15
$$
2. 3 x 3
$$
\begin{aligned}

det(B) = |B| =& 
\begin{vmatrix}
1&3&5 \\
3&8&3 \\
6&3&4
\end{vmatrix} \\
=&1 \times 
\begin{vmatrix}
8&3 \\
3&4
\end{vmatrix}
-
3 \times 
\begin{vmatrix}
3&3 \\
6&4
\end{vmatrix}
+
5 \times
\begin{vmatrix}
3&8\\
6&3
\end{vmatrix} \\
= &1 \times (8 \times 4 - 3 \times 3) - 3 \times (3 \times 4 - 3 \times 6) + 5 \times (3 \times 3 - 8 \times 6) \\
= &1 \times (32-9) - 3 \times (12-18) + 5 \times (9-48) \\
= &23 - 3 \times (-6) + 5 \times (-39) \\
= &23 + 18 - 195 \\
= &-154
\end{aligned}
$$
$
\sum_{i=1}^{\infty}
\prod_{i=1}^n
$


eigenvalue and eigenvector