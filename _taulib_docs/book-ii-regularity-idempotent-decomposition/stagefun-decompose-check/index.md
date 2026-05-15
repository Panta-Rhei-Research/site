---
{
  "projection_kind": "taulib_declaration",
  "title": "stagefun_decompose_check",
  "permalink": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/stagefun-decompose-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::stagefun_decompose_check",
  "declaration_slug": "stagefun-decompose-check",
  "kind": "def",
  "name": "stagefun_decompose_check",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 167,
  "source_line_end": 186,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L167-L186",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
        "url": "/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L167-L186",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/corpus/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L167-L186)
- Source range: L167-L186
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Stagewise decomposition recovery check: the B-part and C-part
    of a StageFun, evaluated and combined as SectorPairs, recover
    the original StageFun evaluation. -/
```

## Source Excerpt

```lean
def stagefun_decompose_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let sf := id_stage
      let (bp, cp) := stagefun_decompose sf
      -- B-part evaluation
      let b_val : SectorPair := ⟨bp.b_fun x k, bp.c_fun x k⟩
      -- C-part evaluation
      let c_val : SectorPair := ⟨cp.b_fun x k, cp.c_fun x k⟩
      -- Original evaluation
      let orig : SectorPair := ⟨sf.b_fun x k, sf.c_fun x k⟩
      -- Recovery: b_val + c_val = orig
      let ok := SectorPair.add b_val c_val == orig
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
