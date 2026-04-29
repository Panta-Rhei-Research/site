---
{
  "projection_kind": "taulib_declaration",
  "title": "majorana_structure",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/majorana-structure/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::majorana_structure",
  "declaration_slug": "majorana-structure",
  "kind": "def",
  "name": "majorana_structure",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 482,
  "source_line_end": 486,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L482-L486",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L482-L486",
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

- Module: [TauLib.BookIV.Electroweak.NeutrinoMode](/verify/taulib/docs/book-iv-electroweak-neutrino-mode/)
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L482-L486)
- Source range: L482-L486
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Majorana structure: all three neutrino modes are Majorana.
    The σ-exchange involution σ: (lobe₁, crossing, lobe₂) → (lobe₂, crossing, lobe₁)
    acts as the exchange matrix [[0,0,1],[0,1,0],[1,0,0]].
    Lab verification (50-digit mpmath):
    - v₁ (λ₁ = 0.016710): σ-even (+1), Majorana
    - v₂ (λ₂ = 0.018734 = a): σ-odd (−1), Majorana via field redefinition
    - v₃ (λ₃ = 0.051318): σ-even (+1), Majorana
    The τ¹ base circle is self-dual (no preferred orientation) =>
    charge conjugation C acts as σ => all modes are self-conjugate. -/
```

## Source Excerpt

```lean
def majorana_structure : String :=
  "All three neutrinos are Majorana. " ++
  "v2=[1,0,-1]/sqrt(2) is sigma-odd (Majorana via phase redefinition). " ++
  "v1 and v3 are sigma-even (Majorana directly). " ++
  "tau^1 self-duality => C acts as sigma-exchange => self-conjugate modes."
```
