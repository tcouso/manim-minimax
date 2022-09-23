$\textbf{function} \, max\_value(s, h):$

$\quad \textbf{if} \, is\_terminal(s) \, \textbf{or} \, h = 0\, \textbf{then return} \, evaluate(s), nill$

$\quad v \leftarrow -\infty$

$\quad move \leftarrow nill$

$\quad \textbf{for each} \, a \, \textbf{in} \, actions(s) \, \textbf{do}$

$\qquad s^* \leftarrow result(s, a)$

$\qquad v_2, a_2 \leftarrow min\_value(s^*, h-1)$

$\qquad \textbf{if} \, v_2 > v \, \textbf{then}$

$\qquad \quad v \leftarrow v_2$

$\qquad \quad move \leftarrow a$

$\quad \textbf{return} \, v, move$


$\textbf{function} \, min\_value(s, h):$

$\quad \textbf{if} \, is\_terminal(s) \, \textbf{then return} \, evaluate(s), nill$

$\quad v \leftarrow +\infty$

$\quad move \leftarrow nill$

$\quad \textbf{for each} \, a \, \textbf{in} \, actions(s) \, \textbf{do}$

$\qquad s^* \leftarrow result(s, a)$

$\qquad v_2, a_2 \leftarrow max\_value(s^*,h-1)$

$\qquad \textbf{if} \, v_2 < v \, \textbf{then}$

$\qquad \quad v \leftarrow v_2$

$\qquad \quad move \leftarrow a$

$\quad \textbf{return} \, v, move$

$\textbf{function} \, max\_value(s):$

$\quad \textbf{if} \, is\_terminal(s) \, \textbf{then return} \, utility(s), nill$

$\quad v \leftarrow -\infty$

$\quad move \leftarrow nill$

$\quad \textbf{for each} \, a \, \textbf{in} \, actions(s) \, \textbf{do}$

$\qquad s^* \leftarrow result(s, a)$

$\qquad v_2, a_2 \leftarrow min\_value(s^*)$

$\qquad \textbf{if} \, v_2 > v \, \textbf{then}$

$\qquad \quad v \leftarrow v_2$

$\qquad \quad move \leftarrow a$

$\quad \textbf{return} \, v, move$


$\textbf{function} \, min\_value(s):$

$\quad \textbf{if} \, is\_terminal(s) \, \textbf{then return} \, utility(s), nill$

$\quad v \leftarrow +\infty$

$\quad move \leftarrow nill$

$\quad \textbf{for each} \, a \, \textbf{in} \, actions(s) \, \textbf{do}$

$\qquad s^* \leftarrow result(s, a)$

$\qquad v_2, a_2 \leftarrow max\_value(s^*)$

$\qquad \textbf{if} \, v_2 < v \, \textbf{then}$

$\qquad \quad v \leftarrow v_2$

$\qquad \quad move \leftarrow a$

$\quad \textbf{return} \, v, move$