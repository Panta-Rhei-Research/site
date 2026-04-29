---
{
  "projection_kind": "taulib_declaration",
  "title": "kleene_rosser_iter_N",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-circularity-full/kleene-rosser-iter-n/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7CircularityFull`.",
  "declaration_id": "TauLib.BookI.Topos.H7CircularityFull::kleene_rosser_iter_N",
  "declaration_slug": "kleene-rosser-iter-n",
  "kind": "theorem",
  "name": "kleene_rosser_iter_N",
  "module_name": "TauLib.BookI.Topos.H7CircularityFull",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/",
  "source_line_start": 104,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L104-L108",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7CircularityFull",
        "url": "/verify/taulib/docs/book-i-topos-h7-circularity-full/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L104-L108",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Topos.H7CircularityFull](/verify/taulib/docs/book-i-topos-h7-circularity-full/)
- Source path: [`TauLib/BookI/Topos/H7CircularityFull.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7CircularityFull.lean#L104-L108)
- Source range: L104-L108
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Kleene-Rosser stabilises at N**: from any seed, after one
    iteration the value is N and stays N forever. -/
```

## Source Excerpt

```lean
theorem kleene_rosser_iter_N (n : Nat) (s : Truth4) :
    cauchyIter kleeneRosserTemplate (n + 1) s = N := by
  induction n with
  | zero => rfl
  | succ k ih => rw [cauchyIter_succ, ih]; rfl
```
