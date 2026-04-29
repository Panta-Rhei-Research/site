---
{
  "projection_kind": "taulib_declaration",
  "title": "ProtonStabilityTheorem",
  "permalink": "/verify/taulib/docs/book-iv-strong-confinement/proton-stability-theorem/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Strong.Confinement`.",
  "declaration_id": "TauLib.BookIV.Strong.Confinement::ProtonStabilityTheorem",
  "declaration_slug": "proton-stability-theorem",
  "kind": "structure",
  "name": "ProtonStabilityTheorem",
  "module_name": "TauLib.BookIV.Strong.Confinement",
  "module_url": "/verify/taulib/docs/book-iv-strong-confinement/",
  "source_line_start": 267,
  "source_line_end": 278,
  "registry_ids": [
    "IV.T72"
  ],
  "related_registry_items": [
    {
      "id": "IV.T72",
      "title": "Proton Stability",
      "url": "/registry/object/IV.T72/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L267-L278",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Strong.Confinement",
        "url": "/verify/taulib/docs/book-iv-strong-confinement/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L267-L278",
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

- Module: [TauLib.BookIV.Strong.Confinement](/verify/taulib/docs/book-iv-strong-confinement/)
- Source path: [`TauLib/BookIV/Strong/Confinement.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Strong/Confinement.lean#L267-L278)
- Source range: L267-L278
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.T72` — Proton Stability

## Immediate Comment / Docstring

```lean
/-- [IV.T72] Proton Stability: the proton is absolutely stable.
    No admissible endomorphism in the 4+1 sector framework can change
    baryon number: B(phi(Psi)) = B(Psi) for all admissible phi.

    This predicts tau_proton = infinity, in contrast to GUT theories
    that predict finite proton lifetime via baryon-number-violating
    leptoquark exchange.

    The proof follows from winding preservation (IV.L8): since phi
    preserves total eta-winding mod 3, and B = (1/3) * sum n_j,
    baryon number is an invariant of admissible dynamics. -/
```

## Source Excerpt

```lean
structure ProtonStabilityTheorem where
  /-- Proton is absolutely stable. -/
  absolutely_stable : Bool := true
  /-- Lifetime prediction: infinite. -/
  lifetime : String := "tau_proton = infinity"
  /-- No baryon number violation by any admissible endomorphism. -/
  no_B_violation : Bool := true
  /-- Contrast with GUTs. -/
  gut_contrast : String := "GUTs predict finite lifetime via leptoquarks"
  /-- Source: winding preservation (IV.L8). -/
  source : String := "follows from winding preservation IV.L8"
  deriving Repr
```
