      Abstract Meaning Representation (AMR) Annotation Release 3.0
                       Linguistic Data Consortium

1.0 Overview

This is the third publication of Abstract Meaning Representation (AMR)
annotation data. It supersedes the previous AMR 2.0 publication
(LDC2017T10).

This corpus comprises a sembank (semantic treebank) of 59255 English
natural language sentences. Each sentence is paired with an AMR graph
that represents its whole-sentence meaning in a tree-structure.

1.1 AMR Description

Meanings are encoded in Abstract Meaning Representation (AMR), a
language described in (Banarescu et al, 2013). AMR utilizes PropBank
frames, non-core semantic roles, within-sentence coreference, named
entity annotation, modality, negation, questions, quantities, and so
on to represent the semantic structure of a sentence largely
independent of its syntax.

More information about AMR, including annotation guidelines, can be
found at http://amr.isi.edu/language.html. Briefly:

  (1) AMRs are rooted, labeled graphs. Like the Penn Treebank, AMRs
  are written in a text format that is readable by people and
  traversable by machines. As a simple example of the format, we
  represent "the boy wants to go" as:

    (w / want-01
      :ARG0 (b / boy)
      :ARG1 (g / go-02
              :ARG0 b))

  which can be paraphrased as: "There is a wanting event (w), whose
  wanter is a boy (b), and whose wanted-thing is a going event (g).
  The entity doing the going is the same boy (b)."

  (2) AMR aims to abstract away from the syntactic structure of
  English, frequently assigning the same AMR to different sentences
  that mean the same thing:

    (a / adjust-01 
     :ARG0 (b / girl) 
     :ARG1 (m / machine)) 

     "The girl made adjustments to the machine."
     "The girl adjusted the machine."
     "The machine was adjusted by the girl."

  (3) AMR incorporates entity recognition, co-reference, and semantic
  roles, but adds significant amounts of further information required
  to represent all of the contents of a sentence. This information
  includes modality, negation, questions, non-core semantic relations
  (e.g. purpose), event relations (e.g. enablement), inverse relations,
  reification, etc.

  (4) AMR makes extensive use of PropBank framesets (Kingsbury and
  Palmer, 2002; Palmer et al., 2005), applying them beyond verbs. For
  example, the phrase "bond investor" is represented with the frame
  "invest-01", even though the phrase contains no verbs:

	(p / person
	  :ARG0-of (i / invest-01
                 :ARG2 (b / bond))

  (5) Single entities typically play multiple roles in an AMR. For
  example, the AMR for "Pascale was charged with public intoxication
  and resisting arrest" contains four instances of the variable "p":

    (c / charge-05
      :ARG1 (p / person
              :name (n / name :op1 "Pascale"))
      :ARG2 (a / and
              :op1 (i / intoxicate-01
                    :ARG1 p
                    :location (p2 / public))
              :op2 (r / resist-01
                     :ARG0 p
                     :ARG1 (a2 / arrest-01
                             :ARG1 p))))

  Such multiple role-playing may represent English pronouns,
  zero-pronouns, or control structures, but may also capture relations
  that are implicit in text.

  (6) AMR is agnostic about how to derive meanings from strings, and
  vice-versa. In translating sentences to AMR, we do not dictate a
  particular sequence of rule applications, or provide alignments that
  reflect such rule sequences. This makes AMR annotation very fast,
  and it allows researchers to explore their own ideas about how
  strings are related to meanings.

  (7) AMR is heavily biased towards English. It is not an Interlingua.

1.2 Major updates in AMR 3.0 from AMR 2.0 (LDC2017T10)

(1) More AMR annotations

  The number of AMR-annotated sentences has increased from 39,260 to
  59,255. NOTE: These numbers *exclude* 6,952 bio AMRs, 1,562 AMRs for
  The Little Prince (available at https://amr.isi.edu/download.html)
  and 1,064 and 1,293 for the blind test sets for SemEval 2015 and
  2016. Most of the newly AMR-annotated sentences are from DEFT
  discussion forum data and selected English sentences from the
  LORELEI corpora.

(2) Deepening AMR

  Hundreds of frames have been added or improved, in particular for
  multi-word predicates such as draw-line-07, read-between-lines-09,
  or take-with-grain-of-salt-36. The new frames have-degree-91 and
  have-quant-91 now better handle comparative and superlative
  constructions, as well as related cases such as "old enough to
  vote", "too short for basketball"; have-degree-of-resemblance-91
  covers constructions such as "(He) is more like (his mother) than
  (his father)." and correlate-91 covers constructions such as "The
  more I practised, the fewer mistakes I made."
		  
(3) Quality control

  The AMR guidelines for annotators have been expanded, especially the
  AMR Dictionary (https://amr.isi.edu/doc/amr-dict.html). The
  automatic AMR Checker has been expanded with numerous new heuristics
  to identify ever more typical annotation errors or
  inconsistencies. Unfortunately however, due to the fact that the
  vast majority of AMRs are single annotations, some inconsistencies
  and errors remain.

(4) Multi-sentence Annotations

  A subset of the corpus (8027 AMRs) have been annotated at the
  document level for coreference, implicit role reference, and
  bridging relations.
  
1.3 Major updates in AMR 2.0 from AMR 1.0 (LDC2014T12)

(1) AMR Wikification

  Named entities in AMR are now marked up with their :wiki values
  where available, linking different surface terms such as "US" and
  "United States of America" to the same entity "United_States".
  Example:
  English: US
  AMR: (c / country :wiki "United_States"
         :name (n / name :op1 "US"))
  English: United States of America
  AMR: (c / country :wiki "United_States"
         :name (n / name :op1 "United" :op2 "States" :op3 "of" :op4 "America"))
  When a named entity has no page on https://en.wikipedia.org/wiki
  the wiki value is a hyphen-minus sign (:wiki "-").

(2) AMR Adoption of New Unified PropBank Frames

  AMR has upgraded all of its old PropBank framesets to the current
  PropBank version, which unifies frames across parts of speech,
  e.g. it has the same frame for 'destroy' and 'destruction'.
  (This unified approach has always been part of AMR's philosophy.)
  See doc/PropBank-unification-notes.txt for more on the latest
  PropBank version.

  PropBank has grown in the number of framesets and in the number of
  senses for a given lemma. AMR has already adopted many of these
  additions and retrofitted AMR annotations to the new frames, but has
  not done so for all new PropBank framesets, particularly not for new
  non-verbal frames, such as "affair" and "(be) fond (of)". AMR will
  continue to adopt new PropBank framesets and retrofit AMR annotations.
  For some PropBank frames, the argument/role structure has changed.

  There are some differences between the original PropBank at UColorado
  and the version used for AMR:

  AMR contains about 40 additional frames, including
    -- role reification frames such as have-purpose-91 and
    -- abstract frames such as have-org-role-91
  that are not part of PropBank. These frames typically do not correspond
  to specific lexical items on the English side.
  (e.g. http://www.isi.edu/~ulf/amr/lib/amr-dict.html#have-org-role-91)

  AMR does not include PropBank frames for words that are decomposable
  such as 'undetectable', which in AMR is annotated using the frames
  for 'possible' and 'detect':
  (p / possible-01 :polarity - :ARG1 (d / detect-01)) or the inverted
  (d / detect-01 :ARG1-of (p / possible-01 :polarity -))

  AMR does not use PropBank roles created to handle discontinuous text
  or separate syntactic nodes; AMR only uses true semantic roles.
  Example:
    (A) Bill Gates is believed to be rich.
    (B) It is believed that Bill Gates is rich.
  Original PropBank for (A):
    arg1: Bill Gates
    rel: believed
    arg2: to be rich
  AMR for both (A) and (B):
    (b / believe-01
      :ARG1 (r / rich
              :domain (p / person :name (n / name :op1 "Bill" :op2 "Gates"))))
  So AMR does not allow the original PropBank's :ARG2 under believe-01.

  The PropBank frames included in this release are a snapshot of the
  version used by AMR at the time of the release. The xml files'
  slot-value pair 'usage="-AMR"' is used to indicate that the xml
  component is not used by AMR, and 'usage="AMR"' is used to indicate
  that the xml component is used only by AMR.

(3) AMR Deepening

  AMR has deepened in a number of ways. For example:
   -- Relational nouns such as 'brother', 'friend' and 'capital' are
      now represented with a new abstract frame have-rel-role-91.
      Example:
         English: "my brother"
         Old AMR: (b / brother :poss (i / i))
         New AMR: (p / person
                    :ARG0-of (h / have-rel-role-91
                               :ARG1 (i / i)
                               :ARG2 (b / brother)))
         (http://www.isi.edu/~ulf/amr/lib/amr-dict.html#have-rel-role-91)
   -- Discourse frame instead-of-91 covers multiple English terms incl.
      "instead of", "in place of", "as opposed to", and "not ... but".
      (http://www.isi.edu/~ulf/amr/lib/amr-dict.html#instead-of-91)

(4) Automatic AMR-English Alignments

  This release includes alignments automatically generated by an
  AMR-English aligner written by Ulf Hermjakob (USC/ISI). These files
  contain tokenized sentences (::tok instead of ::snt). The alignments
  have not been checked by annotators; they are not gold.
  Format info: doc/AMR-alignment-format.txt

(5) Correction of AMR Annotation Errors

  The new version includes corrections of AMR annotation errors in the
  previous versions. Any suspected additional AMR annotation errors
  can be reported via http://amr.isi.edu/report-bug.html .

(6) XML

  Some of the new sentences, especially Discussion Forum (dfb), contain
  XML mark-ups such as &quot; or <a href="http://...">...</a> or <i>a</i>.
  The special frame hyperlink-91 is used to connect a URL to regular text.


2.0 Contents

2.1 Data Profile

The following table summarizes the number of training, dev, and test
AMRs for each dataset in the release. Totals are also provided by
partition and dataset:
  
  Dataset                      Training    Dev    Test    Totals
  --------------------------------------------------------------
  BOLT DF MT (bolt)                1061    133     133      1327
  Broadcast conversation (cctv)     214      0       0       214
  Weblog and WSJ (consensus)          0    100    100        200
  BOLT DF English (dfa)            7379    210    229       7818
  DEFT DF English (dfb)           32915      0      0      32915
  Aesop fables (fables)              49      0      0         49
  Guidelines AMRs (guidelines)      970      0      0        970
  LORELEI (lorelei)                4441    354    527       5322
  2009 Open MT (mt09sdl)            204      0      0        204
  Proxy Reports (proxy)            6603    826    823       8252
  Weblog data (wb)                  866      0      0        866
  Wikipedia (wiki)                  192      0      0        192
  Xinhua MT (xinhua)                741     99     86        926
  --------------------------------------------------------------
  TOTALs                          55635   1722   1898      59255

2.2 File Inventory

  ./data/amrs

Directory containing human-generated AMRs.

  ./data/amrs/split

For those interested in utilizing a standard/community partition for
AMR research (for instance in development of semantic parsers), this
directory contains 59255 AMRs split 93.9%/2.9%/3.2% into
training/dev/test partitions, with most smaller datasets assigned to
one of the splits as a whole. Note that splits observe document
boundaries.

  ./data/amrs/split/dev

Directory containing 1722 dev-partitioned AMRs, across the following 6
dataset files. The number of AMRs in each text file is listed in
parentheses next to the file name:

amr-release-3.0-amrs-dev-bolt.txt (133)
amr-release-3.0-amrs-dev-consensus.txt (100)
amr-release-3.0-amrs-dev-dfa.txt (210)
amr-release-3.0-amrs-dev-lorelei.txt (354)
amr-release-3.0-amrs-dev-proxy.txt (826)
amr-release-3.0-amrs-dev-xinhua.txt (99)

  ./data/amrs/split/test

Directory containing 1898 test-partitioned AMRs, across the following
6 dataset files. The number of AMRs in each text file is listed in
parentheses next to the file name:

amr-release-3.0-amrs-test-bolt.txt (133)
amr-release-3.0-amrs-test-consensus.txt (100)
amr-release-3.0-amrs-test-dfa.txt (229)
amr-release-3.0-amrs-test-lorelei.txt (527)
amr-release-3.0-amrs-test-proxy.txt (823)
amr-release-3.0-amrs-test-xinhua.txt (86)

  ./data/amrs/split/training

Directory containing 55635 training-partitioned AMRs, across the
following 12 dataset files. The number of AMRs in each text file is
listed in parentheses next to the file name:

amr-release-3.0-amrs-training-bolt.txt (1061)
amr-release-3.0-amrs-training-cctv.txt (214)
amr-release-3.0-amrs-training-dfa.txt (7379)
amr-release-3.0-amrs-training-dfb.txt (32915)
amr-release-3.0-amrs-training-fables.txt (49)
amr-release-3.0-amrs-training-guidelines.txt (970)
amr-release-3.0-amrs-training-lorelei.txt (4441)
amr-release-3.0-amrs-training-mt09sdl.txt (204)
amr-release-3.0-amrs-training-proxy.txt (6603)
amr-release-3.0-amrs-training-wb.txt (866)
amr-release-3.0-amrs-training-wiki.txt (192)
amr-release-3.0-amrs-training-xinhua.txt (741)

  ./data/amrs/unsplit

For those not interested in utilizing the training/dev/test AMR
partition, this directory contains the same 59255 AMRs unsplit
(i.e. with no training/dev/test partition), across the following 13
dataset files. The number of AMRs in each text file is listed in
parentheses next to the file name:

amr-release-3.0-amrs-bolt.txt (1327)
amr-release-3.0-amrs-cctv.txt (214)
amr-release-3.0-amrs-consensus.txt (200)
amr-release-3.0-amrs-dfa.txt (7818)
amr-release-3.0-amrs-dfb.txt (32915)
amr-release-3.0-amrs-fables.txt (49)
amr-release-3.0-amrs-guidelines.txt (970)
amr-release-3.0-amrs-lorelei.txt (5322)
amr-release-3.0-amrs-mt09sdl.txt (204)
amr-release-3.0-amrs-proxy.txt (8252)
amr-release-3.0-amrs-wb.txt (866)
amr-release-3.0-amrs-wiki.txt (192)
amr-release-3.0-amrs-xinhua.txt (926)

NOTE: The total number of ./data/amrs/unsplit files is 13, rather than
24, because all the amrs for each workset in the
./data/amrs/split/{dev,test,training} directories are combined into a
*single file* for each workset in in the ./data/amrs/unsplit
directory.

For example, the bolt dataset amrs files in the split directories:
- amr-release-3.0-amrs-dev-bolt.txt
- amr-release-3.0-amrs-test-bolt.txt
- amr-release-3.0-amrs-training-bolt.txt

Are combined into a *single file* in the unsplit directory:
- amr-release-3.0-amrs-bolt.txt

  ./data/alignments

Directory containing token-based alignments automatically generated by
an AMR-English aligner written by Ulf Hermjakob (USC/ISI). These files
contain tokenized sentences (::tok instead of ::snt). The alignments
have not been checked by annotators; they are not gold. Format info,
see AMR-alignment-format.txt in the ./docs directory

  ./data/alignments/split

This directory contains token-based alignments for 59255 AMRs split
into the training/dev/test partitions described above.

  ./data/alignments/split/dev

Directory containing token-based alignments for the same 1722
dev-partitioned AMRs described above, across a corresponding set of 6
alignment files.

  ./data/alignments/split/test

Directory containing token-based alignments for the same 1898
test-partitioned AMRs described above, across a corresponding set of 6
alignment files.

  ./data/alignments/split/training

Directory containing token-based alignments for the same 55635
training-partitioned AMRs described above, across a corresponding set
of 12 alignment files.

  ./data/alignments/unsplit

Directory containing token-based alignments for the same 59255 unsplit
AMRs (described above) across a corresponding set of 13 alignment
files.

  ./data/frames

Directory containing PropBank frames used to annotate the AMRs in this
release.

  ./data/frames/propbank-amr-frames-xml-2018-01-25

Directory containing 5618 XML files for the PropBank frames used to
annotate the AMRs in this release.

  ./data/frames/propbank-amr-frame-arg-descr.txt

Text file containing argument descriptions for the PropBank frames
files in the ./data/frames/propbank-amr-frames-xml-2018-01-25
directory.

  ./data/multisentence

Directory containing human generated, document-level or
"multi-sentence" annotations for a subset of the AMRs in this release
and associated documentation.

  ./data/multisentence/ms-amr-split

For those interested in utilizing a standard/community partition for
multi-sentence AMR research, this directory contains 8027 multi-sentence
AMR annotation files, split 97.5%/2.5% into train/test partitions.

  ./data/multisentence/ms-amr-split/test

Directory containing 201 test-partitioned AMRs, across 9 XML files.

  ./data/multisentence/ms-amr-split/train

Directory containing 7826 train-partitioned AMRs, across 284 XML
files.

  ./data/multisentence/ms-amr-unsplit

For those not interested in utilizing the train/test multi-sentence AMR
partition, this directory contains multi-sentence annotations for the
same 8027 AMRs unsplit (i.e. with no train/test partition), across 293
XML files.

  ./data/multisentence/ms-amr-double-annotations

For those interested in inter-annotator agreement on multi-sentence AMR
annotation, this directory contains alternative multi-sentence AMR
annotations for 588 of the AMRs in the multi-sentence train partition,
across 42 XML files.

  ./data/multisentence/doc/multisentence-amr-notes.txt

Multi-Sentence AMR documentation file, produced by University of
Colorado.

  ./data/multisentence/doc/msamr.dtd

DTD for validating the XML files in the following directories:
./data/multisentence/ms-amr-split
./data/multisentence/ms-amr-double-annotations
./data/multisentence/ms-amr-unsplit

NOTE: This DTD must be copied into the same directory as the
multi-sentence XML files in order for those files to validate against
this DTD.

  ./data/multisentence/doc/msamr-visualizations

Directory containing 335 HTML files containing illustrative
visualizations of the multi-sentence AMR annotations.

  ./docs/AMR-alignment-format.txt

Text file describing the format of the token-based AMR-English
alignment files in the ./data/alignments directory.

  ./docs/PropBank-unification-notes.txt

Text file describing the new Unified (AMR-style) PropBank rolesets
used to produce the AMRs in this release.

  ./docs/amr-guidelines-v1.3.pdf

PDF files of the latest version of the guidelines under which the AMRs
in this release were produced.

  ./docs/frameset.dtd

DTD for validating the XML files in the
./data/frames/propbank-frames-xml-2016-03-08 directory

NOTE: 31 of the propbank XML files do NOT validate against the
frameset.dtd

  ./docs/wiki_docid_entity_url.tsv

TSV file containing the AMR wiki minicorpus docid, Wikipedia-format
named entity, and Wikipedia URL for the 100 Wikipedia pages from which
the 192 "wiki" data sentences in this release originated.

  ./docs/README.txt

This file.

2.3 Structure and content of individual AMRs

Each AMR-sentence pair in the ./data/amrs files comprises the
following data and fields:

  - Header line containing a unique workset-sentence ID for the source
    string that has been AMR annotated (::id), a completion timestamp
    for the AMR (::date), an anonymized ID for the annotator who
    produced the AMR (::annotator), and a marker for the AMRs of
    dually-annotated sentences indicating whether the AMR is the
    preferred representation for the sentence (::preferred)

  - Header line containing the English source sentence that has been
    AMR annotated (::snt)

   - Header line indicating the date on which the AMR was last saved
    (::save-date), and the file name for the AMR-sentence pair
    (::file)

  - Graph containing the manually generated AMR tree for the source
    sentence (see the AMR guidelines for a full description of the
    structure and semantics of AMR graphs).

    NOTE: Proxy report AMRs have an additional field indicating the
    sentence content type (date, country, topic, summary, body, or
    body subordinate) (::snt-type)

    NOTE: The presence of the field-value pair ":script
    amr-snt-id-rep" indicates that the core header information for
    that AMR was restored during processing (based on the filename and
    workset for that AMR). It does not indicate any issues with the
    AMR itself.

    NOTE: AMR graphs may include quoted emoticons, and these may
    include single parentheses, such as ":-)" or ":(". These graphs
    will pass validation as long as they are parsed as lisp-like
    source code, such that the quoted emoticon is escaped. If not, it
    will appear that that parentheses in the graph are unbalanced.


3.0 Source data

The sentences that have been AMR annotated in this release are taken
from the following sources (their dataset shorthand appears in
parentheses).

3.1 BOLT Discussion forum MT data (bolt)

This discussion forum MT data comes from the Bolt Astral team's 2012p1
Tune dataset, and was selected for AMR annotation because it is rich
in informal language, expressions of sentiment and opinion, debates,
power dynamics, and a broader spectrum of events (e.g. communication
events) all of which are not typically found in traditional newswire
data. It also illustrates how AMR is applied to machine translation.

3.2 CCTV Broadcast conversation (cctv)

These transcripts and English translations of Mandarin Chinese
broadcast news conversation from China Central TV (CCTV) were selected
for AMR annotation as they contain a mixture of news content and
conversational features.

3.3 GALE Weblog and Wall Street Journal data (consensus)

This GALE weblog data in this dataset was selected for AMR annotation
because it contains informal language, as well as event phenomena of
interest to events researchers (e.g. causal relations, different
levels or granularities of events, irrealis events, fuzzy temporal
information, etc.)

The Wall Street Journal newswire data in this dataset was selected for
AMR annotation because these sentences contain an interesting
inventory of financial and economic events, and have been widely
annotated within the NLP community. Of the 200 sentences in this
dataset, 100 are from WSJ news, and 100 are GALE Weblog data.

3.4 BOLT Discussion forum English source data (dfa)

This discussion forum data was selected from from LDC's BOLT -
Selected & Segmented Source Data for Annotation R4 corpus (LDC2012R77)
for AMR annotation because it is rich in informal language,
expressions of sentiment and opinion, debates, power dynamics, and a
broader spectrum of events (e.g. communication events) all of which
are not typically found in traditional newswire data.

3.5 DEFT Discussion forum English source data (dfb)

This discussion forum data was selected from Multi-Post Discussion
Forum (MPDF) files collected by LDC, and were selected for AMR
annotation given their selection for annotation in other tasks (ERE,
BeSt, RED, etc) within the DARPA DEFT program. These selected MPDFs
included several high priority documents that were also chosen for
exploratory event annotation in DEFT.

NOTE: For purposes of AMR annotation, these MPDFs were automatically
segmented prior to production. Other DEFT tasks did *NOT* use this
segmentation, as they annotate at the document rather than sentence
level.

3.6 Set of 10 short fables by Aesop (aesop)

This is a new dataset in AMR 3.0, which consists of sentences taken
from 10 short fables by Aesop. Aesop (c. 620 – 564 BCE) was a Greek
fabulist and story teller credited with a number of fables now
collectively known as Aesop's Fables. This AMR dataset was built by
Maximilian Droog-Hayes, Queen Mary University of London.

Reverend George Fyler Townsend (1814–1900) was the translator of the
standard English edition of Aesop's Fables. The text for all of the
stories can either be found on World English or Project Gutenburg: -
http://www.world-english.org/stories.htm - http://www.gutenberg.org/

3.7 Guidelines AMR sentences (guidelines)

This data consists of constructed, example sentences that are used to
for AMR training, and which also appear in the
./docs/amr-guidelines-v1.3.pdf file. They were not selected from an
LDC dataset.

3.8 LORELEI Core/parallel text and SF sentences (lorelei)

This is a new dataset in AMR 3.0, which consists of 5322 English
sentences selected from the LORELEI Parallel Text All Languages
(LDC2016R32) and LORELEI Situation Frame Exercise Annotation
(LDC2017E07) corpora. Of the selected LORELEI sentences, roughly 76%
come from the core/parallel text corpus (LDC2016R32), and 24% come
from the situation frame corpus (LDC2017E07).

These sentences were considered high-priority for AMR annotation
because they had parallel text in many LORELEI languages, and/or had
several layers of associated LORELEI annotation (e.g. situation
frames). See the two corpora above for details.

The AMRs associated with this dataset may be of particular value to
researchers working in under-resourced languages and/or NLP for
situational awareness.

3.9 Open MT Data (mt09sdl)

This data was selected from the NIST 2008-2012 Open Machine
Translation (OpenMT) Progress Test Sets corpus (LDC2013T07) for AMR
annotation because it is rich in events and event-relations commonly
found in newswire data, and illustrates how AMR is applied to machine
translations.

3.10 Narrative text "Proxy Reports" from newswire data (proxy)

This data was selected and segmented from the proxy report data in
LDC's DEFT Narrative Text Source Data R1 corpus (LDC2013E19) for AMR
annotation because they are developed from and thus rich in events and
event-relations commonly found in newswire data, but also have a
templatic, report-like structure which is more difficult for machines
to process.

3.11 GALE-era Weblog data (wb)

The GALE-era weblog data in this dataset was selected for AMR
annotation because it contains informal language, as well as event
phenomena of interest to events researchers (e.g. causal relations,
different levels or granularities of events, irrealis events, fuzzy
temporal information, etc.)

3.12 Wikipedia named entity page sentences (wiki)

This is a new dataset in AMR 3.0, which consists of the lead sentences
from 100 Wikipedia articles about named entities. A list of the
Wikipedia entities and URLs from which the sentences in this dataset
originated can be found in ./docs/wiki_docid_entity_url.tsv

3.13 Translated newswire data from Xinhua (xinhua)

This data was selected from LDC's English Chinese Translation Treebank
v 1.0 corpus (LDC2007T02) for AMR annotation because it is rich in
events and event-relations commonly found in newswire data, and
illustrates how AMR is applied to machine translation.


4.0 Annotation

Annotation for this AMR release was performed by over 25 annotators at
the University of Colorado, the Linguistic Data Consortium, and SDL.

4.1 Guidelines

The most-current version of the AMR guidelines can be found here:
<https://github.com/amrisi/amr-guidelines/blob/master/amr.md>

4.2 The AMR Editor

All AMR annotation is carried out through a web-based editing tool
that encourages speed and consistency. This tool was built by Ulf
Hermjakob at USC/ISI. The AMR Editor:

  1) Supports incremental AMR construction with rapid text-box
  commands.

  2) Highlights concepts that have PropBank framesets, displaying
  those framesets with example sentences.

  3) Pre-processes entities, dates, quantities, etc., making it easy
  for annotators to cut and paste semantic fragments into their AMRs.

  4) Provides annotation guidance, including lists of semantic
  relations (with examples), named entity types, and a search function
  that lets annotators query AMRs that were previously constructed by
  themselves or others. Search queries may be words, phrases, or AMR
  concepts.

  5) Has a built-in AMR Checker that flags typical errors, such as
  misspellings, omissions, illegal relations, etc.
 
  6) Includes administrative support tools for user-account creation,
  sharing of worksets, and annotator activity reports.

More details about the AMR Editor, including tutorial videos, can be
found at <https://amr.isi.edu/editor.html>

5.0 Multi-Sentence AMR

A new feature in AMR 3.0 is the addition of document-level
"multi-sentence" annotations on top of a selected subset of the AMRs in
the ./data/amrs directory.

This multi-sentence annotation layer provides human-generated
coreference, implicit role reference, and bridging (set/member and
part/whole) relationships between AMR variables in different sentences
in the same document.

For details the multi-sentence AMR data in this release, see the
following documentation file in the data directory:

./data/multisentence/doc/multisentence-amr-notes.txt

Multi-Sentence AMR annotation was developed primarily by the
University of Colorado. For more information on multi-sentence AMR,
see the following paper:

  Tim O'Gorman, Michael Regan, Kira Griffitt, Ulf Hermjakob, Kevin
  Knight, and Martha Palmer. 2018. AMR Beyond the Sentence: the
  Multi-sentence AMR corpus. In Proceedings of the 27th International
  Conference on Computational Linguistics (COLING 2018), pages
  3693–3702.

  PDF: http://aclweb.org/anthology/C18-1313


6.0 AMR Contributors
 
AMR was created by Kevin Knight and Ulf Hermjakob at USC Information
Sciences Institute (ISI), in collaboration with Daniel Marcu at SDL,
and Martha Palmer at University of Colorado. University of Colorado,
LDC, and SDL provide ongoing annotation resources and conceptual
collaboration that support development and distribution of AMR
corpora:

Principal AMR contributors:
   Kevin Knight (USC/ISI), Ulf Hermjakob (USC/ISI), Kira Griffitt
   (LDC), Martha Palmer (Univ. of Colorado), Claire Bonial (U.S. Army
   Research Lab), Tim O'Gorman (Univ. of Colorado), Nathan Schneider
   (Georgetown Univ.), Bianca Badarau (SDL), Madalina Bardocz (SDL)
PropBank frames:
   Martha Palmer, Claire Bonial, Tim O'Gorman et al. at University of
   Colorado Boulder
Support in AMR wikification:
   Heng Ji, Xiaoman Pan et al. at Rensselaer Polytechnic Institute (RPI)
AMR annotation supervisors:
   Ulf Hermjakob (USC/ISI), Bianca Badarau (SDL), Tim O'Gorman
   (Univ. of Colorado), Kira Griffitt (LDC)


7.0 Acknowledgments

  From University of Colorado

We gratefully acknowledge the support of the National Science
Foundation Grant NSF: 0910992 IIS:RI: Large: Collaborative Research:
Richer Representations for Machine Translation and the support of
Darpa BOLT - HR0011-11-C-0145 and DEFT - FA-8750-13-2-0045 via a
subcontract from LDC. Any opinions, findings, and conclusions or
recommendations expressed in this material are those of the authors
and do not necessarily reflect the views of the National Science
Foundation, DARPA or the US government.

  From Information Sciences Institute (ISI)

Thanks to NSF (IIS-0908532) for funding the initial design of AMR, and
to DARPA MRP (FA-8750-09-C-0179) for supporting a group to construct
consensus annotations and the AMR Editor. The initial AMR bank was
built under DARPA DEFT FA-8750-13-2-0045 (PI: Stephanie Strassel;
co-PIs: Kevin Knight, Daniel Marcu, and Martha Palmer) and DARPA BOLT
HR0011-12-C-0014 (PI: Kevin Knight).

  From Linguistic Data Consortium (LDC)

This material is based on research sponsored by Air Force Research
Laboratory and Defense Advance Research Projects Agency under
agreement number FA8750-13-2-0045. The U.S. Government is authorized
to reproduce and distribute reprints for Governmental purposes
notwithstanding any copyright notation thereon. The views and
conclusions contained herein are those of the authors and should not
be interpreted as necessarily representing the official policies or
endorsements, either expressed or implied, of Air Force Research
Laboratory and Defense Advanced Research Projects Agency or the
U.S. Government.

We gratefully acknowledge the support of Defense Advanced Research
Projects Agency (DARPA) Machine Reading Program under Air Force
Research Laboratory (AFRL) prime contract no. FA8750-09-C-0184
Subcontract 4400165821. Any opinions, findings, and conclusion or
recommendations expressed in this material are those of the author(s)
and do not necessarily reflect the view of the DARPA, AFRL, or the US
government.

  From Language Weaver (SDL)

This work was partially sponsored by DARPA contract HR0011-11-C-0150
to LanguageWeaver Inc. Any opinions, findings, and conclusion or
recommendations expressed in this material are those of the author(s)
and do not necessarily reflect the view of the DARPA or the US
government.


8.0 AMR links

AMR website: https://amr.isi.edu
AMR public download page: https://amr.isi.edu/download.html (incl. resource lists)
AMR guidelines (overview): https://github.com/amrisi/amr-guidelines/blob/master/amr.md
AMR dictionary (details): https://amr.isi.edu/doc/amr-dict.html
AMR roles: https://amr.isi.edu/doc/roles.html
AMR quantity types: https://amr.isi.edu/doc/quantity-types.html
AMR named entity types: https://amr.isi.edu/doc/ne-types.html
AMR alignment guidelines: https://amr.isi.edu/doc/amr-alignment-guidelines.html
AMR annotation bug report: https://amr.isi.edu/report-bug.html


9.0 Copyright Information

  Portions (c) 1994-1996, 2002-2010 Agence France Presse, Portions (c)
  2007 Al-Ahram, Al Hayat, Al-Quds Al-Arabi, Asharq Al-Awsat, An
  Nahar, Assabah, China Military Online, Chinanews.com, Guangming
  Daily, Xinhua News Agency, Portions (c) 2000 American Broadcasting
  Company, Cable News Network LP, LLLP, National Broadcasting Company,
  Inc., 2000 Public Radio International, Portions (c) 2002-2008, 2010
  The Associated Press, Portions (c) 2003-2004, 2007-2008 Central News
  Agency (Taiwan), Portions (c) 1997, 2004-2007 China Central TV
  (CCTV), Portions (c) 1987-1989 Dow Jones & Company, Inc., Portions
  (c) 1995, 2003, 2005, 2007-2008 Los Angeles Times-Washington Post
  News Service, Inc., Portions (c) 1999, 2002, 2004-2008, 2010 New
  York Times, Portions (c) 1994-1998, 2001-2008 Xinhua News Agency

  (c) 2019 Trustees of the University of Pennsylvania


10.0 Contact Information

For further information about this data release, contact the following
contributors:

  Kevin Knight, ISI/USC                  <knight@isi.edu>               
  --                                     --   
  Bianca Badarau, SDL                    <bbadarau@sdl.com>
  Laura Baranescu, SDL                   <lbanarescu@sdl.com>
  Claire Bonial, U.S. Army Research Lab  <claire.n.bonial.civ@mail.mil>
  Madalina Bardocz, SDL                  <mbardocz@sdl.com>
  Kira Griffitt, LDC                     <kiragrif@ldc.upenn.edu>
  Ulf Hermjakob, ISI/USC                 <ulf@isi.edu>
  Daniel Marcu, ISI/USC                  <marcu@isi.edu>
  Martha Palmer, Univ. of Colorado       <martha.palmer@colorado.edu>
  Tim O'Gorman, Univ. of Colorado        <ogormant@colorado.edu>
  Nathan Schneider, Georgetown Univ.     <nathan.schneider@georgetown.edu>

--------------------------------------------------------------------------
README created by Kira Griffitt on August 8, 2019
README updated by Kira Griffitt on August 8, 2019
README updated by Kira Griffitt on August 11, 2019
README updated by Kira Griffitt on August 12, 2019
README updated by Kira Griffitt on August 13, 2019
