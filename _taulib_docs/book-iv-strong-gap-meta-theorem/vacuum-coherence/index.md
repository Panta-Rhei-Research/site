---
{
  "projection_kind": "taulib_declaration",
  "title": "VacuumCoherence",
  "permalink": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/vacuum-coherence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.GapMetaTheorem`.",
  "declaration_id": "TauLib.BookIV.Strong.GapMetaTheorem::VacuumCoherence",
  "declaration_slug": "vacuum-coherence",
  "kind": "structure",
  "name": "VacuumCoherence",
  "module_name": "TauLib.BookIV.Strong.GapMetaTheorem",
  "module_url": "/verify/taulib/docs/book-iv-strong-gap-meta-theorem/",
  "source_line_start": 250,
  "source_line_end": 255,
  "registry_ids": [
    "IV.L11"
  ],
  "related_registry_items": [
    {
      "id": "IV.L11",
      "title": "Vacuum coherence",
      "url": "/registry/object/IV.L11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L250-L255",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L250-L255",
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
- Source path: [`TauLib/BookIV/Strong/GapMetaTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/GapMetaTheorem.lean#L250-L255)
- Source range: L250-L255
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.L11` — Vacuum coherence

## Immediate Comment / Docstring

```lean
/-- [IV.L11] Vacuum coherence: rho_{n+1->n}(Omega_{n+1}^*) = Omega_n^*. -/
```

## Source Excerpt

```lean
structure VacuumCoherence where
  /-- Restriction preserves vacuum. -/
  restriction_preserves : Bool := true
  /-- Parallels strong vacuum truncation coherence. -/
  parallels : String := "strong vacuum truncation coherence IV.T68"
  deriving Repr
```
