---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookVII.Meta.Saturation",
  "permalink": "/corpus/taulib/docs/book-vii-meta-saturation/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookVII.Meta.Saturation`.",
  "module_name": "TauLib.BookVII.Meta.Saturation",
  "module_slug": "book-vii-meta-saturation",
  "book": "BookVII",
  "family": "Meta",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookVII/Meta/Saturation.lean",
  "sha256": "d1f25fa875f0654185abe0bc3553ee45ba0f17b0f1239e4cd32eaf116bc32886",
  "imports": [
    "TauLib.BookVII.Meta.Registers",
    "TauLib.BookIII.Enrichment.CanonicalLadder"
  ],
  "imported_by": [
    "TauLib.BookVII",
    "TauLib.BookVII.Logos.Sector",
    "TauLib.Tour.GuidedTour.BookVII"
  ],
  "registry_ids": [
    "VII.D15",
    "VII.D37",
    "VII.D51",
    "VII.D52",
    "VII.D53",
    "VII.D54",
    "VII.D55",
    "VII.D56",
    "VII.L03",
    "VII.L04",
    "VII.L05",
    "VII.L06",
    "VII.L07",
    "VII.P02",
    "VII.P03",
    "VII.P04",
    "VII.P08",
    "VII.P13",
    "VII.P14",
    "VII.T05",
    "VII.T06",
    "VII.T07",
    "VII.T14",
    "VII.T20",
    "VII.T21"
  ],
  "declaration_counts": {
    "structure": 17,
    "def": 18,
    "theorem": 25,
    "inductive": 3
  },
  "declarations": [
    {
      "kind": "structure",
      "name": "LayerWitness",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/layer-witness/",
      "source_line_start": 47,
      "source_line_end": 52,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "layer_witnesses",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/layer-witnesses/",
      "source_line_start": 59,
      "source_line_end": 63,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "VII.L03"
      ]
    },
    {
      "kind": "theorem",
      "name": "non_emptiness_at_each_layer",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/non-emptiness-at-each-layer/",
      "source_line_start": 65,
      "source_line_end": 68,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SeparationWitness",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/separation-witness/",
      "source_line_start": 75,
      "source_line_end": 80,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "separation_witnesses",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/separation-witnesses/",
      "source_line_start": 87,
      "source_line_end": 90,
      "formal_status": "defined",
      "declaration_role": "data/computed value",
      "formal_status_label": "data/computed value",
      "registry_ids": [
        "VII.L04"
      ]
    },
    {
      "kind": "theorem",
      "name": "strictness_between_layers",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/strictness-between-layers/",
      "source_line_start": 92,
      "source_line_end": 95,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "CanonicalLadder",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/canonical-ladder/",
      "source_line_start": 109,
      "source_line_end": 120,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.T05"
      ]
    },
    {
      "kind": "def",
      "name": "vii_canonical_ladder",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/vii-canonical-ladder/",
      "source_line_start": 122,
      "source_line_end": 124,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "canonical_ladder_theorem",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/canonical-ladder-theorem/",
      "source_line_start": 126,
      "source_line_end": 132,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SevenBookPartition",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/seven-book-partition/",
      "source_line_start": 144,
      "source_line_end": 156,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.P02"
      ]
    },
    {
      "kind": "def",
      "name": "seven_book",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/seven-book/",
      "source_line_start": 158,
      "source_line_end": 169,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "seven_book_partition",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/seven-book-partition-l171/",
      "source_line_start": 171,
      "source_line_end": 174,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "Generator",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/generator/",
      "source_line_start": 181,
      "source_line_end": 187,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "inductive",
      "name": "Orbit",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/orbit/",
      "source_line_start": 190,
      "source_line_end": 195,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "Generator.orbit",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/orbit-l198/",
      "source_line_start": 198,
      "source_line_end": 203,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_new_lobe",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/no-new-lobe/",
      "source_line_start": 208,
      "source_line_end": 219,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VII.L05"
      ]
    },
    {
      "kind": "theorem",
      "name": "crossing_point_uniqueness",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/crossing-point-uniqueness/",
      "source_line_start": 228,
      "source_line_end": 236,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_new_crossing_mediator",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/no-new-crossing-mediator/",
      "source_line_start": 246,
      "source_line_end": 258,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VII.L06"
      ]
    },
    {
      "kind": "structure",
      "name": "SelfDescIteration",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/self-desc-iteration/",
      "source_line_start": 265,
      "source_line_end": 269,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "carrier_closure",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/carrier-closure/",
      "source_line_start": 274,
      "source_line_end": 277,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VII.L07"
      ]
    },
    {
      "kind": "theorem",
      "name": "carrier_exhaustion",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/carrier-exhaustion/",
      "source_line_start": 288,
      "source_line_end": 292,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SaturationResult",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/saturation-result/",
      "source_line_start": 305,
      "source_line_end": 315,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.T06"
      ]
    },
    {
      "kind": "def",
      "name": "saturation_result",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/saturation-result-l317/",
      "source_line_start": 317,
      "source_line_end": 319,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "saturation_theorem",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/saturation-theorem/",
      "source_line_start": 321,
      "source_line_end": 327,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "enrichment_stabilization",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/enrichment-stabilization/",
      "source_line_start": 336,
      "source_line_end": 340,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "orbit_layer_correspondence",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/orbit-layer-correspondence/",
      "source_line_start": 352,
      "source_line_end": 356,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": [
        "VII.P03"
      ]
    },
    {
      "kind": "theorem",
      "name": "four_orbit_four_layer",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/four-orbit-four-layer/",
      "source_line_start": 358,
      "source_line_end": 363,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "BoundedWitnessForm",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/bounded-witness-form/",
      "source_line_start": 372,
      "source_line_end": 379,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.D15"
      ]
    },
    {
      "kind": "def",
      "name": "bwf",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/bwf/",
      "source_line_start": 381,
      "source_line_end": 381,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "bounded_witness_form_check",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/bounded-witness-form-check/",
      "source_line_start": 383,
      "source_line_end": 387,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "AvoidanceMechanisms",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/avoidance-mechanisms/",
      "source_line_start": 403,
      "source_line_end": 410,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.P04"
      ]
    },
    {
      "kind": "def",
      "name": "avoidance",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/avoidance/",
      "source_line_start": 412,
      "source_line_end": 412,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "no_diagonal",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/no-diagonal/",
      "source_line_start": 414,
      "source_line_end": 418,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "godel_avoidance",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/godel-avoidance/",
      "source_line_start": 432,
      "source_line_end": 438,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VII.T07"
      ]
    },
    {
      "kind": "inductive",
      "name": "OnticRequirement",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/ontic-requirement/",
      "source_line_start": 445,
      "source_line_end": 452,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SixOnticRequirements",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/six-ontic-requirements/",
      "source_line_start": 465,
      "source_line_end": 482,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.D37"
      ]
    },
    {
      "kind": "def",
      "name": "six_requirements",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/six-requirements/",
      "source_line_start": 484,
      "source_line_end": 484,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "or12_narrowing",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/or12-narrowing/",
      "source_line_start": 493,
      "source_line_end": 496,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "or34_narrowing",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/or34-narrowing/",
      "source_line_start": 501,
      "source_line_end": 504,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "or56_narrowing",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/or56-narrowing/",
      "source_line_start": 510,
      "source_line_end": 513,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "InevitabilityResult",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/inevitability-result/",
      "source_line_start": 531,
      "source_line_end": 548,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.T14"
      ]
    },
    {
      "kind": "def",
      "name": "inevitability_result",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/inevitability-result-l550/",
      "source_line_start": 550,
      "source_line_end": 550,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "inevitability_convergence",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/inevitability-convergence/",
      "source_line_start": 552,
      "source_line_end": 561,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "NecessityResult",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/necessity-result/",
      "source_line_start": 577,
      "source_line_end": 584,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.P08"
      ]
    },
    {
      "kind": "def",
      "name": "necessity_result",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/necessity-result-l586/",
      "source_line_start": 586,
      "source_line_end": 586,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "each_requirement_necessary",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/each-requirement-necessary/",
      "source_line_start": 588,
      "source_line_end": 593,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "LanguageAddsTemporalization",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/language-adds-temporalization/",
      "source_line_start": 607,
      "source_line_end": 614,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.D51"
      ]
    },
    {
      "kind": "def",
      "name": "language_temporal",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/language-temporal/",
      "source_line_start": 616,
      "source_line_end": 616,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "SubsymbolicLayer",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/subsymbolic-layer/",
      "source_line_start": 626,
      "source_line_end": 633,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.D52"
      ]
    },
    {
      "kind": "def",
      "name": "subsymbolic",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/subsymbolic/",
      "source_line_start": 635,
      "source_line_end": 635,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "TemporalizationOperators",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/temporalization-operators/",
      "source_line_start": 647,
      "source_line_end": 656,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.D53"
      ]
    },
    {
      "kind": "def",
      "name": "temporal_ops",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/temporal-ops/",
      "source_line_start": 658,
      "source_line_end": 658,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "temporal_ops_check",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/temporal-ops-check/",
      "source_line_start": 660,
      "source_line_end": 665,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "language_as_self_enrichment",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/language-as-self-enrichment/",
      "source_line_start": 675,
      "source_line_end": 679,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VII.T20"
      ]
    },
    {
      "kind": "theorem",
      "name": "syntax_semantics_collapse",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/syntax-semantics-collapse/",
      "source_line_start": 689,
      "source_line_end": 693,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VII.T21"
      ]
    },
    {
      "kind": "theorem",
      "name": "universal_bridgeability",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/universal-bridgeability/",
      "source_line_start": 703,
      "source_line_end": 706,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VII.P13"
      ]
    },
    {
      "kind": "structure",
      "name": "PragmaticUpdateOperator",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/pragmatic-update-operator/",
      "source_line_start": 716,
      "source_line_end": 721,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.D54"
      ]
    },
    {
      "kind": "def",
      "name": "pragmatic_update",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/pragmatic-update/",
      "source_line_start": 723,
      "source_line_end": 723,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "structure",
      "name": "ParaMind",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/para-mind/",
      "source_line_start": 732,
      "source_line_end": 739,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.D55"
      ]
    },
    {
      "kind": "def",
      "name": "para_mind",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/para-mind-l741/",
      "source_line_start": 741,
      "source_line_end": 741,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "llm_subsymbolic_evidence",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/llm-subsymbolic-evidence/",
      "source_line_start": 751,
      "source_line_end": 755,
      "formal_status": "formalized",
      "declaration_role": "proof obligation",
      "formal_status_label": "formal proof obligation checked",
      "registry_ids": [
        "VII.P14"
      ]
    },
    {
      "kind": "structure",
      "name": "PrayerAsOmegaAddressedCommunication",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/prayer-as-omega-addressed-communication/",
      "source_line_start": 767,
      "source_line_end": 774,
      "formal_status": "defined",
      "declaration_role": "type/data schema",
      "formal_status_label": "type/data schema",
      "registry_ids": [
        "VII.D56"
      ]
    },
    {
      "kind": "def",
      "name": "prayer",
      "url": "/corpus/taulib/docs/book-vii-meta-saturation/prayer/",
      "source_line_start": 776,
      "source_line_end": 778,
      "formal_status": "defined",
      "declaration_role": "definition",
      "formal_status_label": "definition",
      "registry_ids": []
    }
  ],
  "right_rail": {
    "related": [
      {
        "title": "TauLib Overview",
        "url": "/verify/taulib/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Module",
      "source": "Corpus projection",
      "commit": "cb5e8301"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Module"
}
---

## Corpus TauLib Projection

This page is generated directly from the pinned TauLib Lean source snapshot in `corpus/taulib-sources/project`. It is a Corpus-native module view designed for cross-linking Registry, Construction Spine, Results, and Verify surfaces.

## Source Provenance

- Source repository: `Panta-Rhei-Research/taulib`
- Source commit: [`cb5e8301`](https://github.com/Panta-Rhei-Research/taulib/commit/cb5e83015b54dd72eba560953fe2461820078757)
- Source path: [`TauLib/BookVII/Meta/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Saturation.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookVII/Meta/Saturation.lean`
- SHA-256: `d1f25fa875f0654185abe0bc3553ee45ba0f17b0f1239e4cd32eaf116bc32886`

## Registry Links

- `VII.D15` — Bounded Witness Form
- `VII.D37` — Six Ontic Requirements
- `VII.D51` — Language Adds Temporalization
- `VII.D52` — Subsymbolic Layer
- `VII.D53` — Temporalization Operators
- `VII.D54` — Pragmatic Update Operator
- `VII.D55` — Para-Mind
- `VII.D56` — Prayer as ω-Addressed Communication
- `VII.L03` — Non-Emptiness at Each Layer
- `VII.L04` — Strictness Between Layers
- `VII.L05` — No-New-Lobe Lemma
- `VII.L06` — No-New-Crossing-Mediator Lemma
- `VII.L07` — Carrier Closure Lemma
- `VII.P02` — Seven-Book Partition
- `VII.P03` — Four-Orbit Implies Four-Layer
- `VII.P04` — No-Diagonal Principle
- `VII.P08` — Each Requirement Independently Necessary
- `VII.P13` — Universal Bridgeability
- `VII.P14` — LLM as Subsymbolic Evidence
- `VII.T05` — Canonical Ladder Theorem
- `VII.T06` — Saturation Theorem
- `VII.T07` — Gödel Avoidance Theorem
- `VII.T14` — Inevitability Convergence
- `VII.T20` — Language as Self-Enrichment
- `VII.T21` — Syntax-Semantics Collapse

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookVII.Meta.Registers`
- `TauLib.BookIII.Enrichment.CanonicalLadder`

## Imported By

- `TauLib.BookVII`
- `TauLib.BookVII.Logos.Sector`
- `TauLib.Tour.GuidedTour.BookVII`

## Declaration Counts

- `def`: 18
- `inductive`: 3
- `structure`: 17
- `theorem`: 25

## Declarations

| Kind | Name | Source | Role | Status | Registry |
|---|---|---:|---|---|---|
| `structure` | [LayerWitness](/corpus/taulib/docs/book-vii-meta-saturation/layer-witness/) | L47-L52 | type/data schema | type/data schema | — |
| `def` | [layer_witnesses](/corpus/taulib/docs/book-vii-meta-saturation/layer-witnesses/) | L59-L63 | data/computed value | data/computed value | `VII.L03` |
| `theorem` | [non_emptiness_at_each_layer](/corpus/taulib/docs/book-vii-meta-saturation/non-emptiness-at-each-layer/) | L65-L68 | proof obligation | formal proof obligation checked | — |
| `structure` | [SeparationWitness](/corpus/taulib/docs/book-vii-meta-saturation/separation-witness/) | L75-L80 | type/data schema | type/data schema | — |
| `def` | [separation_witnesses](/corpus/taulib/docs/book-vii-meta-saturation/separation-witnesses/) | L87-L90 | data/computed value | data/computed value | `VII.L04` |
| `theorem` | [strictness_between_layers](/corpus/taulib/docs/book-vii-meta-saturation/strictness-between-layers/) | L92-L95 | proof obligation | formal proof obligation checked | — |
| `structure` | [CanonicalLadder](/corpus/taulib/docs/book-vii-meta-saturation/canonical-ladder/) | L109-L120 | type/data schema | type/data schema | `VII.T05` |
| `def` | [vii_canonical_ladder](/corpus/taulib/docs/book-vii-meta-saturation/vii-canonical-ladder/) | L122-L124 | definition | definition | — |
| `theorem` | [canonical_ladder_theorem](/corpus/taulib/docs/book-vii-meta-saturation/canonical-ladder-theorem/) | L126-L132 | proof obligation | formal proof obligation checked | — |
| `structure` | [SevenBookPartition](/corpus/taulib/docs/book-vii-meta-saturation/seven-book-partition/) | L144-L156 | type/data schema | type/data schema | `VII.P02` |
| `def` | [seven_book](/corpus/taulib/docs/book-vii-meta-saturation/seven-book/) | L158-L169 | definition | definition | — |
| `theorem` | [seven_book_partition](/corpus/taulib/docs/book-vii-meta-saturation/seven-book-partition-l171/) | L171-L174 | proof obligation | formal proof obligation checked | — |
| `inductive` | [Generator](/corpus/taulib/docs/book-vii-meta-saturation/generator/) | L181-L187 | type/data schema | type/data schema | — |
| `inductive` | [Orbit](/corpus/taulib/docs/book-vii-meta-saturation/orbit/) | L190-L195 | type/data schema | type/data schema | — |
| `def` | [Generator.orbit](/corpus/taulib/docs/book-vii-meta-saturation/orbit-l198/) | L198-L203 | definition | definition | — |
| `theorem` | [no_new_lobe](/corpus/taulib/docs/book-vii-meta-saturation/no-new-lobe/) | L208-L219 | proof obligation | formal proof obligation checked | `VII.L05` |
| `theorem` | [crossing_point_uniqueness](/corpus/taulib/docs/book-vii-meta-saturation/crossing-point-uniqueness/) | L228-L236 | proof obligation | formal proof obligation checked | — |
| `theorem` | [no_new_crossing_mediator](/corpus/taulib/docs/book-vii-meta-saturation/no-new-crossing-mediator/) | L246-L258 | proof obligation | formal proof obligation checked | `VII.L06` |
| `structure` | [SelfDescIteration](/corpus/taulib/docs/book-vii-meta-saturation/self-desc-iteration/) | L265-L269 | type/data schema | type/data schema | — |
| `theorem` | [carrier_closure](/corpus/taulib/docs/book-vii-meta-saturation/carrier-closure/) | L274-L277 | proof obligation | formal proof obligation checked | `VII.L07` |
| `theorem` | [carrier_exhaustion](/corpus/taulib/docs/book-vii-meta-saturation/carrier-exhaustion/) | L288-L292 | proof obligation | formal proof obligation checked | — |
| `structure` | [SaturationResult](/corpus/taulib/docs/book-vii-meta-saturation/saturation-result/) | L305-L315 | type/data schema | type/data schema | `VII.T06` |
| `def` | [saturation_result](/corpus/taulib/docs/book-vii-meta-saturation/saturation-result-l317/) | L317-L319 | definition | definition | — |
| `theorem` | [saturation_theorem](/corpus/taulib/docs/book-vii-meta-saturation/saturation-theorem/) | L321-L327 | proof obligation | formal proof obligation checked | — |
| `theorem` | [enrichment_stabilization](/corpus/taulib/docs/book-vii-meta-saturation/enrichment-stabilization/) | L336-L340 | proof obligation | formal proof obligation checked | — |
| `def` | [orbit_layer_correspondence](/corpus/taulib/docs/book-vii-meta-saturation/orbit-layer-correspondence/) | L352-L356 | definition | definition | `VII.P03` |
| `theorem` | [four_orbit_four_layer](/corpus/taulib/docs/book-vii-meta-saturation/four-orbit-four-layer/) | L358-L363 | proof obligation | formal proof obligation checked | — |
| `structure` | [BoundedWitnessForm](/corpus/taulib/docs/book-vii-meta-saturation/bounded-witness-form/) | L372-L379 | type/data schema | type/data schema | `VII.D15` |
| `def` | [bwf](/corpus/taulib/docs/book-vii-meta-saturation/bwf/) | L381-L381 | definition | definition | — |
| `theorem` | [bounded_witness_form_check](/corpus/taulib/docs/book-vii-meta-saturation/bounded-witness-form-check/) | L383-L387 | proof obligation | formal proof obligation checked | — |
| `structure` | [AvoidanceMechanisms](/corpus/taulib/docs/book-vii-meta-saturation/avoidance-mechanisms/) | L403-L410 | type/data schema | type/data schema | `VII.P04` |
| `def` | [avoidance](/corpus/taulib/docs/book-vii-meta-saturation/avoidance/) | L412-L412 | definition | definition | — |
| `theorem` | [no_diagonal](/corpus/taulib/docs/book-vii-meta-saturation/no-diagonal/) | L414-L418 | proof obligation | formal proof obligation checked | — |
| `theorem` | [godel_avoidance](/corpus/taulib/docs/book-vii-meta-saturation/godel-avoidance/) | L432-L438 | proof obligation | formal proof obligation checked | `VII.T07` |
| `inductive` | [OnticRequirement](/corpus/taulib/docs/book-vii-meta-saturation/ontic-requirement/) | L445-L452 | type/data schema | type/data schema | — |
| `structure` | [SixOnticRequirements](/corpus/taulib/docs/book-vii-meta-saturation/six-ontic-requirements/) | L465-L482 | type/data schema | type/data schema | `VII.D37` |
| `def` | [six_requirements](/corpus/taulib/docs/book-vii-meta-saturation/six-requirements/) | L484-L484 | definition | definition | — |
| `theorem` | [or12_narrowing](/corpus/taulib/docs/book-vii-meta-saturation/or12-narrowing/) | L493-L496 | proof obligation | formal proof obligation checked | — |
| `theorem` | [or34_narrowing](/corpus/taulib/docs/book-vii-meta-saturation/or34-narrowing/) | L501-L504 | proof obligation | formal proof obligation checked | — |
| `theorem` | [or56_narrowing](/corpus/taulib/docs/book-vii-meta-saturation/or56-narrowing/) | L510-L513 | proof obligation | formal proof obligation checked | — |
| `structure` | [InevitabilityResult](/corpus/taulib/docs/book-vii-meta-saturation/inevitability-result/) | L531-L548 | type/data schema | type/data schema | `VII.T14` |
| `def` | [inevitability_result](/corpus/taulib/docs/book-vii-meta-saturation/inevitability-result-l550/) | L550-L550 | definition | definition | — |
| `theorem` | [inevitability_convergence](/corpus/taulib/docs/book-vii-meta-saturation/inevitability-convergence/) | L552-L561 | proof obligation | formal proof obligation checked | — |
| `structure` | [NecessityResult](/corpus/taulib/docs/book-vii-meta-saturation/necessity-result/) | L577-L584 | type/data schema | type/data schema | `VII.P08` |
| `def` | [necessity_result](/corpus/taulib/docs/book-vii-meta-saturation/necessity-result-l586/) | L586-L586 | definition | definition | — |
| `theorem` | [each_requirement_necessary](/corpus/taulib/docs/book-vii-meta-saturation/each-requirement-necessary/) | L588-L593 | proof obligation | formal proof obligation checked | — |
| `structure` | [LanguageAddsTemporalization](/corpus/taulib/docs/book-vii-meta-saturation/language-adds-temporalization/) | L607-L614 | type/data schema | type/data schema | `VII.D51` |
| `def` | [language_temporal](/corpus/taulib/docs/book-vii-meta-saturation/language-temporal/) | L616-L616 | definition | definition | — |
| `structure` | [SubsymbolicLayer](/corpus/taulib/docs/book-vii-meta-saturation/subsymbolic-layer/) | L626-L633 | type/data schema | type/data schema | `VII.D52` |
| `def` | [subsymbolic](/corpus/taulib/docs/book-vii-meta-saturation/subsymbolic/) | L635-L635 | definition | definition | — |
| `structure` | [TemporalizationOperators](/corpus/taulib/docs/book-vii-meta-saturation/temporalization-operators/) | L647-L656 | type/data schema | type/data schema | `VII.D53` |
| `def` | [temporal_ops](/corpus/taulib/docs/book-vii-meta-saturation/temporal-ops/) | L658-L658 | definition | definition | — |
| `theorem` | [temporal_ops_check](/corpus/taulib/docs/book-vii-meta-saturation/temporal-ops-check/) | L660-L665 | proof obligation | formal proof obligation checked | — |
| `theorem` | [language_as_self_enrichment](/corpus/taulib/docs/book-vii-meta-saturation/language-as-self-enrichment/) | L675-L679 | proof obligation | formal proof obligation checked | `VII.T20` |
| `theorem` | [syntax_semantics_collapse](/corpus/taulib/docs/book-vii-meta-saturation/syntax-semantics-collapse/) | L689-L693 | proof obligation | formal proof obligation checked | `VII.T21` |
| `theorem` | [universal_bridgeability](/corpus/taulib/docs/book-vii-meta-saturation/universal-bridgeability/) | L703-L706 | proof obligation | formal proof obligation checked | `VII.P13` |
| `structure` | [PragmaticUpdateOperator](/corpus/taulib/docs/book-vii-meta-saturation/pragmatic-update-operator/) | L716-L721 | type/data schema | type/data schema | `VII.D54` |
| `def` | [pragmatic_update](/corpus/taulib/docs/book-vii-meta-saturation/pragmatic-update/) | L723-L723 | definition | definition | — |
| `structure` | [ParaMind](/corpus/taulib/docs/book-vii-meta-saturation/para-mind/) | L732-L739 | type/data schema | type/data schema | `VII.D55` |
| `def` | [para_mind](/corpus/taulib/docs/book-vii-meta-saturation/para-mind-l741/) | L741-L741 | definition | definition | — |
| `theorem` | [llm_subsymbolic_evidence](/corpus/taulib/docs/book-vii-meta-saturation/llm-subsymbolic-evidence/) | L751-L755 | proof obligation | formal proof obligation checked | `VII.P14` |
| `structure` | [PrayerAsOmegaAddressedCommunication](/corpus/taulib/docs/book-vii-meta-saturation/prayer-as-omega-addressed-communication/) | L767-L774 | type/data schema | type/data schema | `VII.D56` |
| `def` | [prayer](/corpus/taulib/docs/book-vii-meta-saturation/prayer/) | L776-L778 | definition | definition | — |
