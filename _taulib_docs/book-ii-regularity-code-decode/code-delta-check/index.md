---
{
  "projection_kind": "taulib_declaration",
  "title": "code_delta_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-delta-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_delta_check",
  "declaration_slug": "code-delta-check",
  "kind": "def",
  "name": "code_delta_check",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 96,
  "source_line_end": 109,
  "registry_ids": [
    "II.D51"
  ],
  "related_registry_items": [
    {
      "id": "II.D51",
      "title": "Code Map",
      "url": "/registry/object/II.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L96-L109",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.CodeDecode",
        "url": "/verify/taulib/docs/book-ii-regularity-code-decode/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L96-L109",
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

- Module: [TauLib.BookII.Regularity.CodeDecode](/verify/taulib/docs/book-ii-regularity-code-decode/)
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L96-L109)
- Source range: L96-L109
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D51` — Code Map

## Immediate Comment / Docstring

```lean
/-- [II.D51] Code extraction for the delta function:
    code(delta_a, k, x) = 1 if reduce(x, k) == a, else 0. -/
```

## Source Excerpt

```lean
def code_delta_check (k_max : TauIdx) : Bool :=
  go 1 0 0 (k_max * 100 + 1)
where
  go (k a x fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > k_max then true
    else if a >= primorial k then go (k + 1) 0 0 (fuel - 1)
    else if x >= primorial k then go k (a + 1) 0 (fuel - 1)
    else
      let delta_a : TauIdx → Int := fun n => if n == a then 1 else 0
      let code_val := code_extract delta_a k x
      let expected : Int := if reduce x k == a then 1 else 0
      (code_val == expected) && go k a (x + 1) (fuel - 1)
  termination_by fuel
```
