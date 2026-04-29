---
{
  "projection_kind": "taulib_declaration",
  "title": "KoideParameter",
  "permalink": "/verify/taulib/docs/book-iv-particles-three-generations/koide-parameter/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.ThreeGenerations`.",
  "declaration_id": "TauLib.BookIV.Particles.ThreeGenerations::KoideParameter",
  "declaration_slug": "koide-parameter",
  "kind": "structure",
  "name": "KoideParameter",
  "module_name": "TauLib.BookIV.Particles.ThreeGenerations",
  "module_url": "/verify/taulib/docs/book-iv-particles-three-generations/",
  "source_line_start": 244,
  "source_line_end": 253,
  "registry_ids": [
    "IV.D198"
  ],
  "related_registry_items": [
    {
      "id": "IV.D198",
      "title": "Koide parameter",
      "url": "/registry/object/IV.D198/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L244-L253",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.ThreeGenerations",
        "url": "/verify/taulib/docs/book-iv-particles-three-generations/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L244-L253",
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

- Module: [TauLib.BookIV.Particles.ThreeGenerations](/verify/taulib/docs/book-iv-particles-three-generations/)
- Source path: [`TauLib/BookIV/Particles/ThreeGenerations.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/ThreeGenerations.lean#L244-L253)
- Source range: L244-L253
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.D198` — Koide parameter

## Immediate Comment / Docstring

```lean
/-- [IV.D198] The Koide parameter:
    Q = (m_e + m_μ + m_τ) / (√m_e + √m_μ + √m_τ)²

    Discovered by Yoshio Koide in 1982.
    Experimental value: 0.666661 ± 0.000007.

    Numerator and denominator scaled ×10⁶. -/
```

## Source Excerpt

```lean
structure KoideParameter where
  /-- Experimental value numerator (×10⁶). -/
  exp_numer : Nat := 666661
  /-- Denominator (×10⁶). -/
  exp_denom : Nat := 1000000
  /-- Uncertainty (×10⁶). -/
  uncertainty : Nat := 7
  /-- Year of discovery. -/
  year : Nat := 1982
  deriving Repr
```
