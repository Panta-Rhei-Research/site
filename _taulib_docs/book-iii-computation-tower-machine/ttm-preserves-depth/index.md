---
{
  "projection_kind": "taulib_declaration",
  "title": "ttm_preserves_depth",
  "permalink": "/corpus/taulib/docs/book-iii-computation-tower-machine/ttm-preserves-depth/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Computation.TowerMachine`.",
  "declaration_id": "TauLib.BookIII.Computation.TowerMachine::ttm_preserves_depth",
  "declaration_slug": "ttm-preserves-depth",
  "kind": "theorem",
  "name": "ttm_preserves_depth",
  "module_name": "TauLib.BookIII.Computation.TowerMachine",
  "module_url": "/corpus/taulib/docs/book-iii-computation-tower-machine/",
  "source_line_start": 195,
  "source_line_end": 198,
  "registry_ids": [
    "III.D51"
  ],
  "related_registry_items": [
    {
      "id": "III.D51",
      "title": "τ-Tower Machine",
      "url": "/registry/object/III.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L195-L198",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Computation.TowerMachine",
        "url": "/corpus/taulib/docs/book-iii-computation-tower-machine/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L195-L198",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookIII.Computation.TowerMachine](/corpus/taulib/docs/book-iii-computation-tower-machine/)
- Source path: [`TauLib/BookIII/Computation/TowerMachine.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Computation/TowerMachine.lean#L195-L198)
- Source range: L195-L198
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D51` — τ-Tower Machine

## Immediate Comment / Docstring

```lean
/-- [III.D51] Structural: TTM step preserves depth. -/
```

## Source Excerpt

```lean
theorem ttm_preserves_depth (cfg : TTMConfig) :
    (ttm_step cfg).depth = cfg.depth := by
  simp only [ttm_step]
  split <;> (try rfl) <;> split <;> rfl
```
