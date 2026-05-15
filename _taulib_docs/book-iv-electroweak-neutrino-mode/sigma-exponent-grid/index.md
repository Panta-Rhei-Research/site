---
{
  "projection_kind": "taulib_declaration",
  "title": "SigmaExponentGrid",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/sigma-exponent-grid/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::SigmaExponentGrid",
  "declaration_slug": "sigma-exponent-grid",
  "kind": "structure",
  "name": "SigmaExponentGrid",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 597,
  "source_line_end": 604,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L597-L604",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L597-L604",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L597-L604)
- Source range: L597-L604
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Numerical τ-effective: (Δpq=1.16, Δpr=0.87) with r=2.8 gives ratio 32.577 at +7.4 ppm.
    Physical exponents: p=3.67, q=4.83. Rational: Δpq≈29/25, Δpr≈87/100. -/
```

## Source Excerpt

```lean
structure SigmaExponentGrid where
  /-- Grid optimum found. -/
  optimum_found : Bool := true
  /-- Within τ-effective threshold (+7.4 ppm). -/
  tau_effective : Bool := true
  /-- Ratio matches PDG. -/
  ratio_matches : Bool := true
  deriving Repr
```
