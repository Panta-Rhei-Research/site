---
{
  "projection_kind": "taulib_declaration",
  "title": "MajoranaCPPhase",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-cpphase/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::MajoranaCPPhase",
  "declaration_slug": "majorana-cpphase",
  "kind": "structure",
  "name": "MajoranaCPPhase",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 619,
  "source_line_end": 626,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L619-L626",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.NeutrinoMode",
        "url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L619-L626",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L619-L626)
- Source range: L619-L626
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- σ=C_τ fixes Majorana phase φ_Majorana(ν₂) = 0 exactly.
    Proof sketch: σ-odd eigenstate [1,0,-1]/√2 satisfies C_τ·v = -v.
    Majorana condition ψ=Cψ̄ forces e^{iα}=e^{-iα} → α=0 or π.
    ν_middle = σ-odd in normal ordering (V.P127) → φ₂ = 0. -/
```

## Source Excerpt

```lean
structure MajoranaCPPhase where
  /-- φ₂ = 0 exactly. -/
  phi2_zero : Bool := true
  /-- From σ=C_τ constraint. -/
  from_sigma_constraint : Bool := true
  /-- Analytic (not numerical). -/
  is_analytic : Bool := true
  deriving Repr
```
