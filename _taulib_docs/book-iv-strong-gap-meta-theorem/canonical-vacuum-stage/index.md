---
{
  "projection_kind": "taulib_declaration",
  "title": "CanonicalVacuumStage",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/canonical-vacuum-stage/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::CanonicalVacuumStage",
  "declaration_slug": "canonical-vacuum-stage",
  "kind": "structure",
  "name": "CanonicalVacuumStage",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 81,
  "source_line_end": 90,
  "registry_ids": [
    "IV.D163"
  ],
  "related_registry_items": [
    {
      "id": "IV.D163",
      "title": "Canonical vacuum at stage~n",
      "url": "/registry/object/IV.D163/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L81-L90",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L81-L90",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L81-L90)
- Source range: L81-L90
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D163` — Canonical vacuum at stage~n

## Immediate Comment / Docstring

```lean
/-- [IV.D163] Canonical vacuum at stage n:
    Omega_n^* := argmin over C_n^{adm} of (V_n(Omega), code_n(Omega)).
    Lexicographic: first minimize defect, then NF tie-break. -/
```

## Source Excerpt

```lean
structure CanonicalVacuumStage where
  /-- Stage n. -/
  stage : Nat
  /-- Minimizes defect. -/
  minimizes_defect : Bool := true
  /-- NF code tie-breaking. -/
  nf_tiebreak : Bool := true
  /-- Unique by lexicographic total order. -/
  unique : Bool := true
  deriving Repr
```
