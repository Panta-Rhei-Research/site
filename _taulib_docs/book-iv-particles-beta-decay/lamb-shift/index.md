---
{
  "projection_kind": "taulib_declaration",
  "title": "LambShift",
  "permalink": "/verify/taulib/docs/book-iv-particles-beta-decay/lamb-shift/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.BetaDecay`.",
  "declaration_id": "TauLib.BookIV.Particles.BetaDecay::LambShift",
  "declaration_slug": "lamb-shift",
  "kind": "structure",
  "name": "LambShift",
  "module_name": "TauLib.BookIV.Particles.BetaDecay",
  "module_url": "/verify/taulib/docs/book-iv-particles-beta-decay/",
  "source_line_start": 295,
  "source_line_end": 302,
  "registry_ids": [
    "IV.R126"
  ],
  "related_registry_items": [
    {
      "id": "IV.R126",
      "title": "Lamb shift in tau-framework",
      "url": "/registry/object/IV.R126/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L295-L302",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.BetaDecay",
        "url": "/verify/taulib/docs/book-iv-particles-beta-decay/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L295-L302",
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

- Module: [TauLib.BookIV.Particles.BetaDecay](/verify/taulib/docs/book-iv-particles-beta-decay/)
- Source path: [`TauLib/BookIV/Particles/BetaDecay.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/BetaDecay.lean#L295-L302)
- Source range: L295-L302
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R126` — Lamb shift in tau-framework

## Immediate Comment / Docstring

```lean
/-- [IV.R126] The Lamb shift (~1057.845 MHz) is an α_em⁵ · m_e · c²
    effect: vacuum breathing corrections shift s-state energies.
    Conjectural scope: fifth-order holonomy effect on T². -/
```

## Source Excerpt

```lean
structure LambShift where
  /-- Order of correction: α⁵. -/
  alpha_order : Nat := 5
  /-- Frequency (MHz, approx). -/
  freq_mhz : Nat := 1058
  /-- Scope. -/
  scope : String := "conjectural"
  deriving Repr
```
