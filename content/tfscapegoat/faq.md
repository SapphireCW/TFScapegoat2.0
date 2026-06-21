---
title: "FAQ"
weight: 50
icon: "❔"
description: "Contiene tutte le domande più frequenti."
---

## Domande Frequenti

<ul>
	<li><b>D: Cos'è Tag Force Scapegoat?</b></li>
		<ul>
			<li>R: TFScapegoat è una mod per <code>Yu-Gi-Oh! GX Tag Force 1</code> <i>(il gioco per PSP)</i>.  
			La mod vi permetterà di giocare il gioco originale Tag Force con il pool di carte e la banlist del Goat Format. <i>(tutte le altre carte sono state nascoste.)</i> </li>
		</ul>
	<li><b>D: Posso usare il vecchio salvataggio?</b></li>
		<ul>
			<li>R: Certamente! La mod è compatibile con i vecchi salvataggi, l'importante è che il salvataggio sia <code>ULES00600000x</code>.</li>
		</ul>
	<li><b>D: Quali lingue supporta la mod?</b></li>
		<ul>
			<li>R: La mod supporta tutte le lingue supportate dal gioco originale. <i>(<code>Inglese</code>, <code>Tedesco</code>, <code>Francese</code>, <code>Italiano</code> e <code>Spagnolo</code>.)</i></li>
		</ul>
	<li><b>D: La mod funziona solo su emulatore (PPSSPP) o anche su console fisica?</b></li>
		<ul>
			<li>R: La mod funziona con emulatore <code>PPSSPP (v1.20.x)</code> e successive, inoltre la mod funziona anche su console fisica <i>(per maggiori info <a href="https://github.com/xan1242/TFEhpLoader#psp-note">clicca qui!</a>)</i>.</li>
		</ul>
	<li><b>D: Come disinstallo la mod?</b></li>
		<ul>
			<li>R: Per disinstallare la mod vi basterà: cancellare tutti i file importati (<code>Cheats/ULES00600.ini</code>, <code>SAVEDATA/ULES006000001/goat.YGL</code>, <code>PLUGINS/TF-EhpLoader/</code> e sostituire la <code>iso</code> di gioco con quella originale.</li>
		</ul>
	<li><b>D: Cosa succede se acquisto dei pack dallo shop?</b></li>
		<ul>
			<li>R: I pack funzionano normalmente come sul gioco originale, ma tutte le carte non presenti nel pool del Goat vi verranno nascoste e non vi appariranno nella cassa.</li>
		</ul>
	<li id="TFEhpLoader"><b>D: Non mi appare la scritta <i><span style="background-color: green; color: white;">✅Plugin caricato: TF-EhpLoader.prx</span></i> cosa devo fare?</b></li>
	<ul>
		<li>R: Come prima cosa, se l'emulatore non vi carica il plugin, dovete controllare nelle impostazioni di PPSSPP se avete i plugin attivi: per farlo vi basterà recarvi in <code>Impostazioni</code> → <code>Sistema</code> scendere quasi alla fine della pagina e noterete le voci <code>Attiva i Trucchi</code> e <code>Abilita plugin</code> spuntatele entrambe. Riavviate il gioco e adesso dovrebbe comparirvi la scritta<br>
		✅Plugin caricato: TF-EhpLoader.prx.<br>
		Se ancora non vi carica il plugin allora c'è un problema di configurazione del plugin. Recatevi nella cartella <code>memstick</code> della vostra PSP e aprite la cartella <code>PLUGINS</code> → <code>TF-EhpLoader</code> e aprite il file <code>plugin.ini</code> con un blocco note, successivamente dovete controllare se sotto la voce <code>[games]</code> ci sia l'ID di Tag Force 1 <i>(ULES00600 = true)</i>. Se non c'è inseritelo, salvate il file e riavviate l'emulatore.
		<div style="background:#1e3a5f; border-left:4px solid #3498db; padding:15px; margin:20px 0; border-radius:5px;">
			ℹ️ <b>Nota:</b> Se usate entrambe le versioni della mod (sia Tag Force 1, sia Tag Force 5) il file <code>plugin.ini</code> dovrebbe essere così configurato:<br>
			<code>
				[games]<br>
				ULES00600 = true<br>
				ULES01474 = true
			</code>
		</div></li>
	</ul>
	<li><b>D: Il gioco non mi carica i deck modificati degli NPC cosa posso fare?</b></li>
	<ul>
		<li>
			R: Se il gioco non vi carica i deck modificati degli NPC il problema è sicuramente una scorretta configurazione del plugin <code>TFEhpLoader</code>.<br>
			Come prima cosa controllate che all'avvio del gioco vi appaia la scritta:<br>
			<i><span style="background-color: green; color: white;">✅Plugin caricato: TF-EhpLoader.prx</span></i> <i>(date un'occhiata <a href="#TFEhpLoader">qui</a>)</i>.<br>
			Se all'avvio vi compare la scritta ma comunque non vi carica i deck modificati degli NPC allora dobbiamo assicurarci che il tutto funzioni. Rechiamoci nella cartella <code>memstick</code> di PPSSPP e apriamo la cartella <code>PLUGINS</code> → <code>TF-EhpLoader</code> la cartella dovrebbe avere tutti i seguenti file:<br>
			<code>ehps</code> → <code>ULES00600</code> → <code>rcpset.ehp</code><br>
			<code>plugin.ini</code>, <code>TF-EhpLoader.prx</code> e <code>TF-EhpLoaderBoot.prx</code>.<br>
			Se il tutto è configurato nel seguente modo allora è corretto e il tutto funziona. Altrimenti se vi manca qualche file riscaricate la cartella PLUGINS dalla pagina di <a href="/tfscapegoat/download">download</a>
		</li>
	</ul>
	<li><b>D: Il gioco non mi carica la banlist del Goat Format cosa posso fare?</b></li>
	<ul>
		<li>
			R: Se il gioco non vi carica la banlist del Goat dovete innanzitutto assicurarvi di averla caricata correttamente: Recatevi nella cartella <code>memstick</code> di PPSSPP e aprite la cartella <code>SAVEDATA</code> → <code>ULES006000001</code> e assicuratevi che ci sia il file <code>goat.YGL</code> <i>(Se il file non è stato caricato potete riscaricarlo dalla pagina di <a href="/tfscapegoat/download">download</a>)</i>.<br>
			Invece se il file è presente nella cartella ma il gioco non vi carica la banlist le soluzioni possono essere:<br>
			1) Seguire il passo <a href="/tfscapegoat/guida/#passo-4">4.</a> della guida per impostare la banlist.<br>
			2) controllare nelle impostazioni di PPSSPP se avete i trucchi attivi: per farlo vi basterà recarvi in <code>Impostazioni</code> → <code>Sistema</code> scendere quasi alla fine della pagina e noterete la voce <code>Attiva i Trucchi</code> ora se non attiva attivatela. Riavviate il gioco, seguite il passo <a href="/tfscapegoat/guida/#passo-4">4.</a> della guida e dovrebbe funzionare tutto correttamente.<br>
			3) controllare nel menù dei trucchi PPSSPP se il trucco <code>Allows Game To Read Decrypted DLC Files (ULES00600 v1.01)</code> sia attivo.
		</li>
	</ul>
</ul>

<div style="background:#5c4a1f; border-left:4px solid #f39c12; padding:15px; margin:20px 0; border-radius:5px;">
⚠️ <b>Attenzione:</b> Se avete altre segnalazioni potete contattarci al seguente indirizzo e-mail: <a href="mailto:tfscapegoat.info@protonmail.com">tfscapegoat.info@protonmail.com</a> oppure <a href="/contattaci">clicca qui!</a>
</div>