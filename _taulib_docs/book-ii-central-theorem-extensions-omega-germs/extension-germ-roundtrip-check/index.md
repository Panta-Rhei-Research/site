---
{
  "projection_kind": "taulib_declaration",
  "title": "extension_germ_roundtrip_check",
  "permalink": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/extension-germ-roundtrip-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms`.",
  "declaration_id": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms::extension_germ_roundtrip_check",
  "declaration_slug": "extension-germ-roundtrip-check",
  "kind": "def",
  "name": "extension_germ_roundtrip_check",
  "module_name": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
  "module_url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/",
  "source_line_start": 215,
  "source_line_end": 237,
  "registry_ids": [
    "II.T38"
  ],
  "related_registry_items": [
    {
      "id": "II.T38",
      "title": "Extensions Are Omega-Germ Transformers",
      "url": "/registry/object/II.T38/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L215-L237",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms",
        "url": "/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L215-L237",
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

- Module: [TauLib.BookII.CentralTheorem.ExtensionsOmegaGerms](/verify/taulib/docs/book-ii-central-theorem-extensions-omega-germs/)
- Source path: [`TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/CentralTheorem/ExtensionsOmegaGerms.lean#L215-L237)
- Source range: L215-L237
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T38` — Extensions Are Omega-Germ Transformers

## Immediate Comment / Docstring

```lean
/-- [II.T38] Extension-germ roundtrip: extracting the omega-germ from
    an extension and reconstructing the extension from the germ give
    the same result.

    Step 1 (Code direction): Given bndlift extension, extract the
    Code at stage k: code_extract(bndlift_fn, k, x) = bndlift(reduce(x, k), k-1)
    for the bndlift "function" viewed as a map on stage-k inputs.

    Step 2 (Decode direction): Reconstruct from the coded values:
    decode_reconstruct(coded_table, k, x) should give back the
    original bndlift value.

    The roundtrip works because Code/Decode is a bijection (II.T35)
    and bndlift is well-defined on residue classes (depends only on
    reduce(x, k)). -/
```

## Source Excerpt

```lean
def extension_germ_roundtrip_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k >= db then go (x + 1) 1 (fuel - 1)
    else
      -- The bndlift at stage k as a function: f(n) = bndlift(n, k) as Int
      let bnd_fn : TauIdx -> Int := fun n => (bndlift n k : Int)
      -- Code: extract at stage k+1
      let coded := code_extract bnd_fn (k + 1) x
      -- Direct bndlift at the reduced input
      let direct := (bndlift (reduce x (k + 1)) k : Int)
      -- Should match: code_extract evaluates at reduce(x, k+1)
      let code_ok := coded == direct
      -- Decode roundtrip: decode(code(bnd_fn), k+1, x) should give bnd_fn(reduce(x, k+1))
      let coded_table : TauIdx -> Int := fun a => code_extract bnd_fn (k + 1) a
      let decoded := decode_reconstruct coded_table (k + 1) x
      let expected := bnd_fn (reduce x (k + 1))
      let decode_ok := decoded == expected
      code_ok && decode_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
