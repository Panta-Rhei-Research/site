---
{
  "projection_kind": "taulib_declaration",
  "title": "non_trivial_check",
  "permalink": "/verify/taulib/docs/book-ii-interior-tau3-fibration/non-trivial-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.Tau3Fibration`.",
  "declaration_id": "TauLib.BookII.Interior.Tau3Fibration::non_trivial_check",
  "declaration_slug": "non-trivial-check",
  "kind": "def",
  "name": "non_trivial_check",
  "module_name": "TauLib.BookII.Interior.Tau3Fibration",
  "module_url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/",
  "source_line_start": 130,
  "source_line_end": 142,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L130-L142",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.Tau3Fibration",
        "url": "/verify/taulib/docs/book-ii-interior-tau3-fibration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L130-L142",
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

- Module: [TauLib.BookII.Interior.Tau3Fibration](/verify/taulib/docs/book-ii-interior-tau3-fibration/)
- Source path: [`TauLib/BookII/Interior/Tau3Fibration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/Tau3Fibration.lean#L130-L142)
- Source range: L130-L142
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T03, clause 3] Non-triviality: demonstrate that the fibration
    is NOT a product bundle by showing different base points yield
    different fiber behavior.

    Example: X=12 has (A=3, D=4) while X=64 has (A=2, D=1).
    At A=3: B can be up to what 3^B allows.
    At A=2: B can be up to what 2^B allows (different range). -/
```

## Source Excerpt

```lean
def non_trivial_check : Bool :=
  -- Same base A=2 but very different fibers
  let p1 := from_tau_idx 4    -- (2, 2, 1, 1)
  let p2 := from_tau_idx 16   -- (2, 1, 3, 1)
  let p3 := from_tau_idx 64   -- (2, 3, 2, 1)
  -- All have A=2 but different (B,C) combinations
  p1.a == p2.a && p2.a == p3.a &&
  (p1.b, p1.c) != (p2.b, p2.c) &&
  (p2.b, p2.c) != (p3.b, p3.c) &&
  -- Different A leads to fundamentally different structure
  let q1 := from_tau_idx 12   -- (3, 1, 1, 4)
  let q2 := from_tau_idx 27   -- (3, 3, 1, 1)
  q1.a == q2.a && q1.a != p1.a
```
