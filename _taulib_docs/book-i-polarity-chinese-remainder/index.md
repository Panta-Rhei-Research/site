---
{
  "projection_kind": "taulib_module",
  "title": "TauLib.BookI.Polarity.ChineseRemainder",
  "permalink": "/verify/taulib/docs/book-i-polarity-chinese-remainder/",
  "summary_short": "Corpus-native TauLib projection for `TauLib.BookI.Polarity.ChineseRemainder`.",
  "module_name": "TauLib.BookI.Polarity.ChineseRemainder",
  "module_slug": "book-i-polarity-chinese-remainder",
  "book": "BookI",
  "family": "Polarity",
  "source_repo": "Panta-Rhei-Research/taulib",
  "source_commit": "cb5e83015b54dd72eba560953fe2461820078757",
  "source_path": "taulib-sources/project/TauLib/BookI/Polarity/ChineseRemainder.lean",
  "sha256": "39e098da837e072e707c156c8f4965a0ed47fbfb9b109d307080c69e0a33c3ea",
  "imports": [
    "TauLib.BookI.Polarity.ModArith",
    "TauLib.BookI.Polarity.ExtGCD"
  ],
  "imported_by": [
    "TauLib.BookI",
    "TauLib.BookI.Boundary.Galois",
    "TauLib.BookI.Holomorphy.TauHolomorphic",
    "TauLib.BookI.Polarity.CRTBasis",
    "TauLib.BookI.Polarity.PrimePolarityClassifier",
    "TauLib.BookI.Polarity.TeichmuellerLift",
    "TauLib.BookI.Topos.LimitsSites"
  ],
  "registry_ids": [
    "I.D28",
    "I.D29"
  ],
  "declaration_counts": {
    "def": 17,
    "theorem": 2,
    "example": 85,
    "eval": 21
  },
  "declarations": [
    {
      "kind": "def",
      "name": "mod_inv_go",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv-go/",
      "source_line_start": 40,
      "source_line_end": 44,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "mod_inv",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv/",
      "source_line_start": 47,
      "source_line_end": 47,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_inv_go_correct",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv-go-correct/",
      "source_line_start": 54,
      "source_line_end": 71,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "theorem",
      "name": "mod_inv_correct",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv-correct/",
      "source_line_start": 74,
      "source_line_end": 84,
      "formal_status": "formalized",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_decompose",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-decompose/",
      "source_line_start": 92,
      "source_line_end": 93,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_basis",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-basis/",
      "source_line_start": 102,
      "source_line_end": 106,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_reconstruct_go",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-reconstruct-go/",
      "source_line_start": 113,
      "source_line_end": 121,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_reconstruct",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-reconstruct/",
      "source_line_start": 124,
      "source_line_end": 125,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_basis_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-basis-check/",
      "source_line_start": 132,
      "source_line_end": 133,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_roundtrip_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-roundtrip-check/",
      "source_line_start": 136,
      "source_line_end": 137,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_coherence_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-coherence-check/",
      "source_line_start": 141,
      "source_line_end": 143,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_exhaustive_check_go",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-exhaustive-check-go/",
      "source_line_start": 146,
      "source_line_end": 150,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_exhaustive_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-exhaustive-check/",
      "source_line_start": 152,
      "source_line_end": 153,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_idempotent_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-idempotent-check/",
      "source_line_start": 160,
      "source_line_end": 163,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_orthogonal_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-orthogonal-check/",
      "source_line_start": 166,
      "source_line_end": 167,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_partition_go",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-partition-go/",
      "source_line_start": 170,
      "source_line_end": 174,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_partition_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-partition-check/",
      "source_line_start": 176,
      "source_line_end": 177,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l185/",
      "source_line_start": 185,
      "source_line_end": 185,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l186/",
      "source_line_start": 186,
      "source_line_end": 186,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l187/",
      "source_line_start": 187,
      "source_line_end": 187,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l189/",
      "source_line_start": 189,
      "source_line_end": 189,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l190/",
      "source_line_start": 190,
      "source_line_end": 190,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l191/",
      "source_line_start": 191,
      "source_line_end": 191,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l193/",
      "source_line_start": 193,
      "source_line_end": 193,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l194/",
      "source_line_start": 194,
      "source_line_end": 194,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l195/",
      "source_line_start": 195,
      "source_line_end": 195,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l198/",
      "source_line_start": 198,
      "source_line_end": 198,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l199/",
      "source_line_start": 199,
      "source_line_end": 199,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l200/",
      "source_line_start": 200,
      "source_line_end": 200,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l201/",
      "source_line_start": 201,
      "source_line_end": 201,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l202/",
      "source_line_start": 202,
      "source_line_end": 202,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l203/",
      "source_line_start": 203,
      "source_line_end": 203,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l204/",
      "source_line_start": 204,
      "source_line_end": 204,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l205/",
      "source_line_start": 205,
      "source_line_end": 205,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l206/",
      "source_line_start": 206,
      "source_line_end": 206,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l207/",
      "source_line_start": 207,
      "source_line_end": 207,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l208/",
      "source_line_start": 208,
      "source_line_end": 208,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l209/",
      "source_line_start": 209,
      "source_line_end": 209,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l210/",
      "source_line_start": 210,
      "source_line_end": 210,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l211/",
      "source_line_start": 211,
      "source_line_end": 211,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l212/",
      "source_line_start": 212,
      "source_line_end": 212,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l213/",
      "source_line_start": 213,
      "source_line_end": 213,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l216/",
      "source_line_start": 216,
      "source_line_end": 216,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l217/",
      "source_line_start": 217,
      "source_line_end": 217,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l218/",
      "source_line_start": 218,
      "source_line_end": 218,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l219/",
      "source_line_start": 219,
      "source_line_end": 219,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l220/",
      "source_line_start": 220,
      "source_line_end": 220,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l227/",
      "source_line_start": 227,
      "source_line_end": 227,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l228/",
      "source_line_start": 228,
      "source_line_end": 228,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l229/",
      "source_line_start": 229,
      "source_line_end": 229,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l230/",
      "source_line_start": 230,
      "source_line_end": 230,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l231/",
      "source_line_start": 231,
      "source_line_end": 231,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l232/",
      "source_line_start": 232,
      "source_line_end": 232,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l233/",
      "source_line_start": 233,
      "source_line_end": 233,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l234/",
      "source_line_start": 234,
      "source_line_end": 234,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l235/",
      "source_line_start": 235,
      "source_line_end": 235,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l238/",
      "source_line_start": 238,
      "source_line_end": 238,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l239/",
      "source_line_start": 239,
      "source_line_end": 239,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l240/",
      "source_line_start": 240,
      "source_line_end": 240,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l241/",
      "source_line_start": 241,
      "source_line_end": 241,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l242/",
      "source_line_start": 242,
      "source_line_end": 242,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l243/",
      "source_line_start": 243,
      "source_line_end": 243,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l246/",
      "source_line_start": 246,
      "source_line_end": 246,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l247/",
      "source_line_start": 247,
      "source_line_end": 247,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l248/",
      "source_line_start": 248,
      "source_line_end": 248,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l249/",
      "source_line_start": 249,
      "source_line_end": 249,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l250/",
      "source_line_start": 250,
      "source_line_end": 250,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l257/",
      "source_line_start": 257,
      "source_line_end": 257,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l258/",
      "source_line_start": 258,
      "source_line_end": 258,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l259/",
      "source_line_start": 259,
      "source_line_end": 259,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l260/",
      "source_line_start": 260,
      "source_line_end": 260,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l261/",
      "source_line_start": 261,
      "source_line_end": 261,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l262/",
      "source_line_start": 262,
      "source_line_end": 262,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l264/",
      "source_line_start": 264,
      "source_line_end": 264,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l265/",
      "source_line_start": 265,
      "source_line_end": 265,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l266/",
      "source_line_start": 266,
      "source_line_end": 266,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l267/",
      "source_line_start": 267,
      "source_line_end": 267,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l268/",
      "source_line_start": 268,
      "source_line_end": 268,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l270/",
      "source_line_start": 270,
      "source_line_end": 270,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l271/",
      "source_line_start": 271,
      "source_line_end": 271,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l272/",
      "source_line_start": 272,
      "source_line_end": 272,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l273/",
      "source_line_start": 273,
      "source_line_end": 273,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l274/",
      "source_line_start": 274,
      "source_line_end": 274,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l275/",
      "source_line_start": 275,
      "source_line_end": 275,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l278/",
      "source_line_start": 278,
      "source_line_end": 278,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l279/",
      "source_line_start": 279,
      "source_line_end": 279,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l280/",
      "source_line_start": 280,
      "source_line_end": 280,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l287/",
      "source_line_start": 287,
      "source_line_end": 287,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l288/",
      "source_line_start": 288,
      "source_line_end": 288,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l289/",
      "source_line_start": 289,
      "source_line_end": 289,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l290/",
      "source_line_start": 290,
      "source_line_end": 290,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l291/",
      "source_line_start": 291,
      "source_line_end": 291,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l292/",
      "source_line_start": 292,
      "source_line_end": 292,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l293/",
      "source_line_start": 293,
      "source_line_end": 293,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l294/",
      "source_line_start": 294,
      "source_line_end": 294,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l295/",
      "source_line_start": 295,
      "source_line_end": 295,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_add_hom_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-add-hom-check/",
      "source_line_start": 302,
      "source_line_end": 307,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "def",
      "name": "crt_mul_hom_check",
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-mul-hom-check/",
      "source_line_start": 310,
      "source_line_end": 315,
      "formal_status": "defined",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l318/",
      "source_line_start": 318,
      "source_line_end": 318,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l319/",
      "source_line_start": 319,
      "source_line_end": 319,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l320/",
      "source_line_start": 320,
      "source_line_end": 320,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l323/",
      "source_line_start": 323,
      "source_line_end": 323,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l324/",
      "source_line_start": 324,
      "source_line_end": 324,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "example",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l325/",
      "source_line_start": 325,
      "source_line_end": 325,
      "formal_status": "example",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l332/",
      "source_line_start": 332,
      "source_line_end": 332,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l333/",
      "source_line_start": 333,
      "source_line_end": 333,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l334/",
      "source_line_start": 334,
      "source_line_end": 334,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l335/",
      "source_line_start": 335,
      "source_line_end": 335,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l338/",
      "source_line_start": 338,
      "source_line_end": 338,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l339/",
      "source_line_start": 339,
      "source_line_end": 339,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l340/",
      "source_line_start": 340,
      "source_line_end": 340,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l343/",
      "source_line_start": 343,
      "source_line_end": 343,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l344/",
      "source_line_start": 344,
      "source_line_end": 344,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l347/",
      "source_line_start": 347,
      "source_line_end": 347,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l348/",
      "source_line_start": 348,
      "source_line_end": 348,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l349/",
      "source_line_start": 349,
      "source_line_end": 349,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l352/",
      "source_line_start": 352,
      "source_line_end": 352,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l353/",
      "source_line_start": 353,
      "source_line_end": 353,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l354/",
      "source_line_start": 354,
      "source_line_end": 354,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l357/",
      "source_line_start": 357,
      "source_line_end": 357,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l358/",
      "source_line_start": 358,
      "source_line_end": 358,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l361/",
      "source_line_start": 361,
      "source_line_end": 361,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l364/",
      "source_line_start": 364,
      "source_line_end": 364,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l365/",
      "source_line_start": 365,
      "source_line_end": 365,
      "formal_status": "computed",
      "registry_ids": []
    },
    {
      "kind": "eval",
      "name": null,
      "url": "/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l366/",
      "source_line_start": 366,
      "source_line_end": 368,
      "formal_status": "computed",
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
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean",
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
- Source path: [`TauLib/BookI/Polarity/ChineseRemainder.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ChineseRemainder.lean)
- Corpus snapshot path: `taulib-sources/project/TauLib/BookI/Polarity/ChineseRemainder.lean`
- SHA-256: `39e098da837e072e707c156c8f4965a0ed47fbfb9b109d307080c69e0a33c3ea`

## Registry Links

- `I.D28` — Boundary Local Ring
- `I.D29` — CRT Decomposition

## Construction Spine Links

- No Construction Spine step is currently mapped to this module.

## Imports

- `TauLib.BookI.Polarity.ModArith`
- `TauLib.BookI.Polarity.ExtGCD`

## Imported By

- `TauLib.BookI`
- `TauLib.BookI.Boundary.Galois`
- `TauLib.BookI.Holomorphy.TauHolomorphic`
- `TauLib.BookI.Polarity.CRTBasis`
- `TauLib.BookI.Polarity.PrimePolarityClassifier`
- `TauLib.BookI.Polarity.TeichmuellerLift`
- `TauLib.BookI.Topos.LimitsSites`

## Declaration Counts

- `def`: 17
- `eval`: 21
- `example`: 85
- `theorem`: 2

## Declarations

| Kind | Name | Source | Status | Registry |
|---|---|---:|---|---|
| `def` | [mod_inv_go](/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv-go/) | L40-L44 | defined | — |
| `def` | [mod_inv](/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv/) | L47-L47 | defined | — |
| `theorem` | [mod_inv_go_correct](/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv-go-correct/) | L54-L71 | formalized | — |
| `theorem` | [mod_inv_correct](/verify/taulib/docs/book-i-polarity-chinese-remainder/mod-inv-correct/) | L74-L84 | formalized | — |
| `def` | [crt_decompose](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-decompose/) | L92-L93 | defined | — |
| `def` | [crt_basis](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-basis/) | L102-L106 | defined | — |
| `def` | [crt_reconstruct_go](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-reconstruct-go/) | L113-L121 | defined | — |
| `def` | [crt_reconstruct](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-reconstruct/) | L124-L125 | defined | — |
| `def` | [crt_basis_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-basis-check/) | L132-L133 | defined | — |
| `def` | [crt_roundtrip_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-roundtrip-check/) | L136-L137 | defined | — |
| `def` | [crt_coherence_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-coherence-check/) | L141-L143 | defined | — |
| `def` | [crt_exhaustive_check_go](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-exhaustive-check-go/) | L146-L150 | defined | — |
| `def` | [crt_exhaustive_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-exhaustive-check/) | L152-L153 | defined | — |
| `def` | [crt_idempotent_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-idempotent-check/) | L160-L163 | defined | — |
| `def` | [crt_orthogonal_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-orthogonal-check/) | L166-L167 | defined | — |
| `def` | [crt_partition_go](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-partition-go/) | L170-L174 | defined | — |
| `def` | [crt_partition_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-partition-check/) | L176-L177 | defined | — |
| `example` | [#eval L185](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l185/) | L185-L185 | example | — |
| `example` | [#eval L186](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l186/) | L186-L186 | example | — |
| `example` | [#eval L187](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l187/) | L187-L187 | example | — |
| `example` | [#eval L189](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l189/) | L189-L189 | example | — |
| `example` | [#eval L190](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l190/) | L190-L190 | example | — |
| `example` | [#eval L191](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l191/) | L191-L191 | example | — |
| `example` | [#eval L193](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l193/) | L193-L193 | example | — |
| `example` | [#eval L194](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l194/) | L194-L194 | example | — |
| `example` | [#eval L195](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l195/) | L195-L195 | example | — |
| `example` | [#eval L198](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l198/) | L198-L198 | example | — |
| `example` | [#eval L199](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l199/) | L199-L199 | example | — |
| `example` | [#eval L200](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l200/) | L200-L200 | example | — |
| `example` | [#eval L201](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l201/) | L201-L201 | example | — |
| `example` | [#eval L202](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l202/) | L202-L202 | example | — |
| `example` | [#eval L203](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l203/) | L203-L203 | example | — |
| `example` | [#eval L204](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l204/) | L204-L204 | example | — |
| `example` | [#eval L205](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l205/) | L205-L205 | example | — |
| `example` | [#eval L206](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l206/) | L206-L206 | example | — |
| `example` | [#eval L207](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l207/) | L207-L207 | example | — |
| `example` | [#eval L208](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l208/) | L208-L208 | example | — |
| `example` | [#eval L209](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l209/) | L209-L209 | example | — |
| `example` | [#eval L210](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l210/) | L210-L210 | example | — |
| `example` | [#eval L211](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l211/) | L211-L211 | example | — |
| `example` | [#eval L212](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l212/) | L212-L212 | example | — |
| `example` | [#eval L213](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l213/) | L213-L213 | example | — |
| `example` | [#eval L216](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l216/) | L216-L216 | example | — |
| `example` | [#eval L217](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l217/) | L217-L217 | example | — |
| `example` | [#eval L218](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l218/) | L218-L218 | example | — |
| `example` | [#eval L219](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l219/) | L219-L219 | example | — |
| `example` | [#eval L220](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l220/) | L220-L220 | example | — |
| `example` | [#eval L227](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l227/) | L227-L227 | example | — |
| `example` | [#eval L228](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l228/) | L228-L228 | example | — |
| `example` | [#eval L229](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l229/) | L229-L229 | example | — |
| `example` | [#eval L230](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l230/) | L230-L230 | example | — |
| `example` | [#eval L231](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l231/) | L231-L231 | example | — |
| `example` | [#eval L232](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l232/) | L232-L232 | example | — |
| `example` | [#eval L233](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l233/) | L233-L233 | example | — |
| `example` | [#eval L234](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l234/) | L234-L234 | example | — |
| `example` | [#eval L235](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l235/) | L235-L235 | example | — |
| `example` | [#eval L238](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l238/) | L238-L238 | example | — |
| `example` | [#eval L239](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l239/) | L239-L239 | example | — |
| `example` | [#eval L240](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l240/) | L240-L240 | example | — |
| `example` | [#eval L241](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l241/) | L241-L241 | example | — |
| `example` | [#eval L242](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l242/) | L242-L242 | example | — |
| `example` | [#eval L243](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l243/) | L243-L243 | example | — |
| `example` | [#eval L246](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l246/) | L246-L246 | example | — |
| `example` | [#eval L247](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l247/) | L247-L247 | example | — |
| `example` | [#eval L248](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l248/) | L248-L248 | example | — |
| `example` | [#eval L249](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l249/) | L249-L249 | example | — |
| `example` | [#eval L250](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l250/) | L250-L250 | example | — |
| `example` | [#eval L257](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l257/) | L257-L257 | example | — |
| `example` | [#eval L258](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l258/) | L258-L258 | example | — |
| `example` | [#eval L259](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l259/) | L259-L259 | example | — |
| `example` | [#eval L260](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l260/) | L260-L260 | example | — |
| `example` | [#eval L261](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l261/) | L261-L261 | example | — |
| `example` | [#eval L262](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l262/) | L262-L262 | example | — |
| `example` | [#eval L264](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l264/) | L264-L264 | example | — |
| `example` | [#eval L265](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l265/) | L265-L265 | example | — |
| `example` | [#eval L266](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l266/) | L266-L266 | example | — |
| `example` | [#eval L267](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l267/) | L267-L267 | example | — |
| `example` | [#eval L268](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l268/) | L268-L268 | example | — |
| `example` | [#eval L270](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l270/) | L270-L270 | example | — |
| `example` | [#eval L271](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l271/) | L271-L271 | example | — |
| `example` | [#eval L272](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l272/) | L272-L272 | example | — |
| `example` | [#eval L273](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l273/) | L273-L273 | example | — |
| `example` | [#eval L274](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l274/) | L274-L274 | example | — |
| `example` | [#eval L275](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l275/) | L275-L275 | example | — |
| `example` | [#eval L278](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l278/) | L278-L278 | example | — |
| `example` | [#eval L279](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l279/) | L279-L279 | example | — |
| `example` | [#eval L280](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l280/) | L280-L280 | example | — |
| `example` | [#eval L287](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l287/) | L287-L287 | example | — |
| `example` | [#eval L288](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l288/) | L288-L288 | example | — |
| `example` | [#eval L289](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l289/) | L289-L289 | example | — |
| `example` | [#eval L290](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l290/) | L290-L290 | example | — |
| `example` | [#eval L291](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l291/) | L291-L291 | example | — |
| `example` | [#eval L292](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l292/) | L292-L292 | example | — |
| `example` | [#eval L293](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l293/) | L293-L293 | example | — |
| `example` | [#eval L294](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l294/) | L294-L294 | example | — |
| `example` | [#eval L295](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l295/) | L295-L295 | example | — |
| `def` | [crt_add_hom_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-add-hom-check/) | L302-L307 | defined | — |
| `def` | [crt_mul_hom_check](/verify/taulib/docs/book-i-polarity-chinese-remainder/crt-mul-hom-check/) | L310-L315 | defined | — |
| `example` | [#eval L318](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l318/) | L318-L318 | example | — |
| `example` | [#eval L319](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l319/) | L319-L319 | example | — |
| `example` | [#eval L320](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l320/) | L320-L320 | example | — |
| `example` | [#eval L323](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l323/) | L323-L323 | example | — |
| `example` | [#eval L324](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l324/) | L324-L324 | example | — |
| `example` | [#eval L325](/verify/taulib/docs/book-i-polarity-chinese-remainder/example-l325/) | L325-L325 | example | — |
| `eval` | [#eval L332](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l332/) | L332-L332 | computed | — |
| `eval` | [#eval L333](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l333/) | L333-L333 | computed | — |
| `eval` | [#eval L334](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l334/) | L334-L334 | computed | — |
| `eval` | [#eval L335](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l335/) | L335-L335 | computed | — |
| `eval` | [#eval L338](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l338/) | L338-L338 | computed | — |
| `eval` | [#eval L339](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l339/) | L339-L339 | computed | — |
| `eval` | [#eval L340](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l340/) | L340-L340 | computed | — |
| `eval` | [#eval L343](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l343/) | L343-L343 | computed | — |
| `eval` | [#eval L344](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l344/) | L344-L344 | computed | — |
| `eval` | [#eval L347](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l347/) | L347-L347 | computed | — |
| `eval` | [#eval L348](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l348/) | L348-L348 | computed | — |
| `eval` | [#eval L349](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l349/) | L349-L349 | computed | — |
| `eval` | [#eval L352](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l352/) | L352-L352 | computed | — |
| `eval` | [#eval L353](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l353/) | L353-L353 | computed | — |
| `eval` | [#eval L354](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l354/) | L354-L354 | computed | — |
| `eval` | [#eval L357](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l357/) | L357-L357 | computed | — |
| `eval` | [#eval L358](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l358/) | L358-L358 | computed | — |
| `eval` | [#eval L361](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l361/) | L361-L361 | computed | — |
| `eval` | [#eval L364](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l364/) | L364-L364 | computed | — |
| `eval` | [#eval L365](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l365/) | L365-L365 | computed | — |
| `eval` | [#eval L366](/verify/taulib/docs/book-i-polarity-chinese-remainder/eval-l366/) | L366-L368 | computed | — |
