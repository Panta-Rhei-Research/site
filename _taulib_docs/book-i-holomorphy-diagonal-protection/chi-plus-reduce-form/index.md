---
{
  "projection_kind": "taulib_declaration",
  "title": "chi_plus_reduce_form",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-diagonal-protection/chi-plus-reduce-form/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.DiagonalProtection`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DiagonalProtection::chi_plus_reduce_form",
  "declaration_slug": "chi-plus-reduce-form",
  "kind": "def",
  "name": "chi_plus_reduce_form",
  "module_name": "TauLib.BookI.Holomorphy.DiagonalProtection",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-diagonal-protection/",
  "source_line_start": 103,
  "source_line_end": 106,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L103-L106",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DiagonalProtection",
        "url": "/corpus/taulib/docs/book-i-holomorphy-diagonal-protection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L103-L106",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Holomorphy.DiagonalProtection](/corpus/taulib/docs/book-i-holomorphy-diagonal-protection/)
- Source path: [`TauLib/BookI/Holomorphy/DiagonalProtection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DiagonalProtection.lean#L103-L106)
- Source range: L103-L106
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- χ₊ has reduce form with b_map = id, c_map = const 0. -/
```

## Source Excerpt

```lean
def chi_plus_reduce_form : ReduceForm chi_plus_stage :=
  ⟨fun n => n, fun _ => 0,
   fun n k => by simp [chi_plus_stage],
   fun _ k => by simp [chi_plus_stage, reduce, Nat.zero_mod]⟩
```
