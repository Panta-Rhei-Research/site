---
{
  "projection_kind": "taulib_declaration",
  "title": "neutrino_exponent_43_ratio",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/neutrino-exponent-43-ratio/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::neutrino_exponent_43_ratio",
  "declaration_slug": "neutrino-exponent-43-ratio",
  "kind": "def",
  "name": "neutrino_exponent_43_ratio",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 684,
  "source_line_end": 686,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L684-L686",
  "formal_status": "defined",
  "declaration_role": "docstring/data record",
  "formal_status_label": "docstring/data record",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L684-L686",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "docstring/data record",
      "status": "docstring/data record"
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L684-L686)
- Source range: L684-L686
- Kind: `def`
- Public role: `docstring/data record`
- Formal status hint: `docstring/data record`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- 4/3 ratio from lemniscate counting: Δpq/Δpr = (2×lobes)/sectors = 4/3.
    Span Δpq+Δpr = 2 = |lobes|. Gives (8/7, 6/7) with n=7 (same as Higgs).
    Numerically: ratio=30.21 at -72589 ppm from PDG 32.576 (conjectural). -/
```

## Source Excerpt

```lean
def neutrino_exponent_43_ratio : String :=
  "Δpq/Δpr = 4/3 = (2×lobes)/sectors = 4/3; span=2=|lobes|; (8/7,6/7) with n=7. " ++
  "Same lemniscate counting as Higgs n=7. Numerically -72589 ppm (conjectural)."
```
