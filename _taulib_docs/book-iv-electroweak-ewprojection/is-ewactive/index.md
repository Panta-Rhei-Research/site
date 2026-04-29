---
{
  "projection_kind": "taulib_declaration",
  "title": "isEWActive",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-ewprojection/is-ewactive/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.EWProjection`.",
  "declaration_id": "TauLib.BookIV.Electroweak.EWProjection::isEWActive",
  "declaration_slug": "is-ewactive",
  "kind": "def",
  "name": "isEWActive",
  "module_name": "TauLib.BookIV.Electroweak.EWProjection",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/",
  "source_line_start": 66,
  "source_line_end": 70,
  "registry_ids": [
    "IV.D335"
  ],
  "related_registry_items": [
    {
      "id": "IV.D335",
      "title": "EW-Active Mode",
      "url": "/registry/object/IV.D335/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L66-L70",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.EWProjection",
        "url": "/verify/taulib/docs/book-iv-electroweak-ewprojection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L66-L70",
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

- Module: [TauLib.BookIV.Electroweak.EWProjection](/verify/taulib/docs/book-iv-electroweak-ewprojection/)
- Source path: [`TauLib/BookIV/Electroweak/EWProjection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/EWProjection.lean#L66-L70)
- Source range: L66-L70
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `IV.D335` — EW-Active Mode

## Immediate Comment / Docstring

```lean
/-- [IV.D335] EW-active: a boundary mode participates in electroweak mixing.

    **Rule:** B-sector (γ, all configs) + A-sector charged (π, lobe configs).
    Uses sector assignment and polarity, not SM physics.
    - B-sector (EM): always EW-active (EM IS electroweak)
    - A-sector (Weak): lobes = W± (charged, EW-active), crossing = Z⁰ (neutral, not EW-active)
    - All others: not EW-active (strong, gravity, Higgs) -/
```

## Source Excerpt

```lean
def isEWActive : BoundaryMode → Bool
  | ⟨.gamma, _⟩         => true   -- B-sector: always EW-active
  | ⟨.pi_, .lobePos⟩    => true   -- A-sector, W⁺: charged, EW-active
  | ⟨.pi_, .lobeNeg⟩    => true   -- A-sector, W⁻: charged, EW-active
  | _                    => false  -- All else: not EW-active
```
