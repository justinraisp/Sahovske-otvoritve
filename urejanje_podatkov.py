import csv
import os
import re
import json

vzorec_bloka = re.compile(
    r'<tr id="yui-rec\d+" class="(yui-dt-(first|last) )?yui-dt-(odd|even)" style="">.*?'
    r'</div></td></tr>',
    re.DOTALL
)

vzorec_otvoritve = re.compile(
    r'<td headers="yui-dt0-th-name " class="yui-dt0-col-name yui-dt-col-name yui-dt-asc yui-dt-sortable yui-dt-first"><div class="yui-dt-liner"><a href="/gamedb/opening/\d+">(?P<otvoritev>.+?)</a></div></td>'
    r'<td headers="yui-dt0-th-moves_san " class="yui-dt0-col-moves_san yui-dt-col-moves_san"><div class="yui-dt-liner"><div style="width:30px;background-color:(?P<barva>.+?);">&nbsp;</div></div></td>'
    r'<td headers="yui-dt0-th-total_games " class="yui-dt0-col-total_games yui-dt-col-total_games yui-dt-sortable"><div class="yui-dt-liner">(?P<stevilo_iger>.+?)</div></td>'
    r'<td headers="yui-dt0-th-eco " class="yui-dt0-col-eco yui-dt-col-eco yui-dt-sortable"><div class="yui-dt-liner">(?P<eco>.+?)</div></td>'
    r'<td headers="yui-dt0-th-last_played " class="yui-dt0-col-last_played yui-dt-col-last_played"><div class="yui-dt-liner">(?P<datum>.+?)</div></td>'
    r'<td headers="yui-dt0-th-performance " class="yui-dt0-col-performance yui-dt-col-performance yui-dt-sortable"><div class="yui-dt-liner">(?P<performance_rating>.+?)</div></td>'
    r'<td headers="yui-dt0-th-avg_player " class="yui-dt0-col-avg_player yui-dt-col-avg_player yui-dt-sortable"><div class="yui-dt-liner">(?P<povprecen_rating>.+?)</div></td>'
    r'<td headers="yui-dt0-th-player_wins " class="yui-dt0-col-player_wins yui-dt-col-player_wins yui-dt-sortable"><div class="yui-dt-liner">(?P<zmaga>.+?)</div></td>'
    r'<td headers="yui-dt0-th-draws " class="yui-dt0-col-draws yui-dt-col-draws yui-dt-sortable"><div class="yui-dt-liner">(?P<remi>.+?)</div></td>'
    r'<td headers="yui-dt0-th-opponent_wins " class="yui-dt0-col-opponent_wins yui-dt-col-opponent_wins yui-dt-sortable"><div class="yui-dt-liner">(?P<poraz>.+?)</div>'
    r'</td><td headers="yui-dt0-th-moves_san " class="yui-dt0-col-moves_san yui-dt-col-moves_san yui-dt-last"><div class="yui-dt-liner">(?P<poteze>.+?)</div></td></tr>',
    flags=re.DOTALL
)
vse_otvoritve = []
for i in range(4):
    with open(f"otvoritve\index_otvoritve{i}.html", "r", encoding="utf-8") as f:
        vsebina = f.read()
        print(len(vzorec_otvoritve.findall(vsebina)))
        for blok in vzorec_bloka.finditer(vsebina):
            otvoritev = vzorec_otvoritve.search(blok.group(0)).groupdict()
            vse_otvoritve.append(otvoritev)


print(vse_otvoritve[0])
print(len(vse_otvoritve))

