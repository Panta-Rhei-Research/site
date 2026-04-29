---
{
  "projection_kind": "taulib_declaration",
  "title": "sprint4a_oqc3_status",
  "permalink": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/sprint4a-oqc3-status/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Electroweak.NeutrinoMode`.",
  "declaration_id": "TauLib.BookIV.Electroweak.NeutrinoMode::sprint4a_oqc3_status",
  "declaration_slug": "sprint4a-oqc3-status",
  "kind": "def",
  "name": "sprint4a_oqc3_status",
  "module_name": "TauLib.BookIV.Electroweak.NeutrinoMode",
  "module_url": "/verify/taulib/docs/book-iv-electroweak-neutrino-mode/",
  "source_line_start": 568,
  "source_line_end": 571,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L568-L571",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L568-L571",
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
- Source path: [`TauLib/BookIV/Electroweak/NeutrinoMode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/NeutrinoMode.lean#L568-L571)
- Source range: L568-L571
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- OQ-C3 status after Sprint 4A:
    (1) Normal ordering proven analytically from r < p (τ-effective).
    (2) σ-odd eigenvalue = ι_τ^p is exact (not numerical).
    (3) One-parameter family gives 39.45 (not 32.58): pure integer steps insufficient.
    (4) Key open: why Δpq=1.1 ≠ Δpr=0.9?
    (5) PMNS requires A-sector rotation (Sprint 5).
    CF candidate: q ≈ 5 - 1/a₃ where a₃=13 from CF[ι_τ⁻¹]=[2;1,1,1,13,...]. -/
```

## Source Excerpt

```lean
def sprint4a_oqc3_status : String :=
  "Sprint 4A: normal ordering proven (tau-effective, r<p). " ++
  "sigma-odd eigenval = iota^p exact. 1-param family gives 39.45 (not 32.58). " ++
  "Open: Delta_pq != Delta_pr asymmetry origin. PMNS: A-sector rotation needed (Sprint 5)."
```
