---
{
  "projection_kind": "taulib_declaration",
  "title": "higgs_satisfies_kh",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/higgs-satisfies-kh/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::higgs_satisfies_kh",
  "declaration_slug": "higgs-satisfies-kh",
  "kind": "def",
  "name": "higgs_satisfies_kh",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 280,
  "source_line_end": 281,
  "registry_ids": [
    "IV.P100"
  ],
  "related_registry_items": [
    {
      "id": "IV.P100",
      "title": "Higgs sector satisfies (KH-1)--(KH-3)",
      "url": "/registry/object/IV.P100/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L280-L281",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.GapMetaTheorem",
        "url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L280-L281",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Strong.GapMetaTheorem](/verify/taulib/docs/book-iv-strong-gap-meta-theorem/)
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L280-L281)
- Source range: L280-L281
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.P100` — Higgs sector satisfies (KH-1)--(KH-3)

## Immediate Comment / Docstring

```lean
/-- [IV.P100] The Higgs sector satisfies all three kernel hypotheses
    with stabilization at n_* = 2 (primorial depth of B). -/
```

## Source Excerpt

```lean
def higgs_satisfies_kh : KernelHypotheses where
  stabilization_horizon := 2
```
