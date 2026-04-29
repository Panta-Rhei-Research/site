---
{
  "projection_kind": "taulib_declaration",
  "title": "TruncationCoherence",
  "permalink": "/verify/taulib/docs/book-iv-strong-strong-vacuum/truncation-coherence/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.StrongVacuum`.",
  "declaration_id": "TauLib.BookIV.Strong.StrongVacuum::TruncationCoherence",
  "declaration_slug": "truncation-coherence",
  "kind": "structure",
  "name": "TruncationCoherence",
  "module_name": "TauLib.BookIV.Strong.StrongVacuum",
  "module_url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/",
  "source_line_start": 286,
  "source_line_end": 293,
  "registry_ids": [
    "IV.T68"
  ],
  "related_registry_items": [
    {
      "id": "IV.T68",
      "title": "Truncation coherence for Γ*_s",
      "url": "/registry/object/IV.T68/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L286-L293",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.StrongVacuum",
        "url": "/verify/taulib/docs/book-iv-strong-strong-vacuum/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L286-L293",
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

- Module: [TauLib.BookIV.Strong.StrongVacuum](/verify/taulib/docs/book-iv-strong-strong-vacuum/)
- Source path: [`TauLib/BookIV/Strong/StrongVacuum.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/StrongVacuum.lean#L286-L293)
- Source range: L286-L293
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T68` — Truncation coherence for Γ*_s

## Immediate Comment / Docstring

```lean
/-- [IV.T68] Truncation coherence: for all n >= 3, the restriction
    of the strong vacuum at stage n+1 to stage n recovers the
    strong vacuum at stage n: Gamma_s^*[n+1]|_n = Gamma_s^*[n].

    This ensures the projective limit is well-defined. -/
```

## Source Excerpt

```lean
structure TruncationCoherence where
  /-- Coherence holds for all n >= activation_depth. -/
  activation_depth : Nat := 3
  /-- Restriction of (n+1)-vacuum equals n-vacuum. -/
  restriction_preserves : Bool := true
  /-- Mechanism: argmin + NFMin commute with restriction. -/
  mechanism : String := "argmin and NFMin commute with restriction maps"
  deriving Repr
```
