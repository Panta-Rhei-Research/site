---
{
  "projection_kind": "taulib_declaration",
  "title": "OmegaTail.mul",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-ring/mul/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.OmegaRing`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaRing::OmegaTail.mul",
  "declaration_slug": "mul",
  "kind": "def",
  "name": "OmegaTail.mul",
  "module_name": "TauLib.BookI.Polarity.OmegaRing",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-ring/",
  "source_line_start": 189,
  "source_line_end": 193,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L189-L193",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaRing",
        "url": "/verify/taulib/docs/book-i-polarity-omega-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L189-L193",
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

- Module: [TauLib.BookI.Polarity.OmegaRing](/verify/taulib/docs/book-i-polarity-omega-ring/)
- Source path: [`TauLib/BookI/Polarity/OmegaRing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L189-L193)
- Source range: L189-L193
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- General componentwise multiplication of two omega-tails of equal depth. -/
```

## Source Excerpt

```lean
def OmegaTail.mul (t1 t2 : OmegaTail) (_hd : t1.depth = t2.depth) : OmegaTail where
  depth := t1.depth
  components := (List.range t1.depth).map (fun i =>
    (t1.components.getD i 0 * t2.components.getD i 0) % primorial (i + 1))
  depth_eq := by simp
```
