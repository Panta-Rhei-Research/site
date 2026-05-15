---
{
  "projection_kind": "taulib_declaration",
  "title": "IsHyperfactWitness",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-hyperfact-prop/is-hyperfact-witness/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.HyperfactProp`.",
  "declaration_id": "TauLib.BookI.Coordinates.HyperfactProp::IsHyperfactWitness",
  "declaration_slug": "is-hyperfact-witness",
  "kind": "def",
  "name": "IsHyperfactWitness",
  "module_name": "TauLib.BookI.Coordinates.HyperfactProp",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-hyperfact-prop/",
  "source_line_start": 73,
  "source_line_end": 76,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L73-L76",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.HyperfactProp",
        "url": "/corpus/taulib/docs/book-i-coordinates-hyperfact-prop/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L73-L76",
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

- Module: [TauLib.BookI.Coordinates.HyperfactProp](/corpus/taulib/docs/book-i-coordinates-hyperfact-prop/)
- Source path: [`TauLib/BookI/Coordinates/HyperfactProp.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/HyperfactProp.lean#L73-L76)
- Source range: L73-L76
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `IsHyperfactWitness x a b c d v`: the tuple (a, b, c, d) is a
    valid hyperfactorization of `x`, with `v = b · A↑↑(c-1)` being
    the A-adic valuation of `x/d`, and `A↑↑c` does NOT divide `v`
    (the C-maximality condition required by No-Tie). -/
```

## Source Excerpt

```lean
def IsHyperfactWitness (x a b c d v : TauIdx) : Prop :=
  ValidABCD x a b c d
    ∧ b * tetration a (c - 1) = v
    ∧ ¬ (tetration a c ∣ v)
```
